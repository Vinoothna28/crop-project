from datetime import datetime, timezone

from pymongo import MongoClient
from pymongo.errors import (
    ConnectionFailure,
    PyMongoError,
    ServerSelectionTimeoutError
)

from config import (
    MONGO_URI,
    MONGO_DB_NAME,
    MONGO_COLLECTION_NAME,
    MONGO_HISTORY_COLLECTION
)


# ---------------------------------------------------------
# MongoDB client
# ---------------------------------------------------------

_client = None


def get_database():
    """
    Create a reusable MongoDB connection and return the
    configured database.

    The connection is created only once and reused during
    the Streamlit session.
    """

    global _client

    if not MONGO_URI:
        raise ValueError(
            "MONGO_URI is missing. "
            "Please configure MongoDB Atlas in your .env file."
        )

    try:

        if _client is None:

            _client = MongoClient(
                MONGO_URI,
                serverSelectionTimeoutMS=5000,
                connectTimeoutMS=5000
            )

        # Check whether MongoDB is reachable.
        _client.admin.command("ping")

        return _client[MONGO_DB_NAME]

    except (ConnectionFailure, ServerSelectionTimeoutError) as error:

        raise ConnectionError(
            "Unable to connect to MongoDB Atlas. "
            "Check your connection string, network access, "
            "and Atlas cluster status."
        ) from error

    except PyMongoError as error:

        raise RuntimeError(
            f"MongoDB error: {error}"
        ) from error


# ---------------------------------------------------------
# Collections
# ---------------------------------------------------------

def get_disease_collection():
    """
    Return the disease knowledge-base collection.
    """

    database = get_database()

    return database[MONGO_COLLECTION_NAME]


def get_history_collection():
    """
    Return the anonymous prediction history collection.
    """

    database = get_database()

    return database[MONGO_HISTORY_COLLECTION]


# ---------------------------------------------------------
# Disease knowledge base
# ---------------------------------------------------------

def find_disease(model_label):
    """
    Find a disease knowledge-base record using the label
    returned by the AI model.

    Example:
        Tomato___Early_blight

    Returns:
        MongoDB document or None
    """

    if not model_label:
        return None

    try:

        collection = get_disease_collection()

        document = collection.find_one(
            {
                "model_labels": model_label
            }
        )

        return document

    except PyMongoError as error:

        raise RuntimeError(
            f"Unable to query disease knowledge base: {error}"
        ) from error


# ---------------------------------------------------------
# Disease lookup by crop
# ---------------------------------------------------------

def find_diseases_by_crop(crop):
    """
    Return all disease records belonging to a crop.

    Example:
        Tomato
    """

    if not crop:
        return []

    try:

        collection = get_disease_collection()

        documents = collection.find(
            {
                "crop": {
                    "$regex": f"^{crop}$",
                    "$options": "i"
                }
            }
        )

        return list(documents)

    except PyMongoError as error:

        raise RuntimeError(
            f"Unable to retrieve crop diseases: {error}"
        ) from error


# ---------------------------------------------------------
# Insert / update disease knowledge
# ---------------------------------------------------------

def seed_disease(document):
    """
    Insert a disease into the knowledge base.

    If the disease already exists, update it instead of
    creating a duplicate record.
    """

    if not document:
        raise ValueError("Disease document cannot be empty.")

    if "disease_id" not in document:
        raise ValueError(
            "Disease document must contain disease_id."
        )

    try:

        collection = get_disease_collection()

        result = collection.update_one(
            {
                "disease_id": document["disease_id"]
            },
            {
                "$set": document
            },
            upsert=True
        )

        return {
            "matched": result.matched_count,
            "modified": result.modified_count,
            "upserted_id": (
                str(result.upserted_id)
                if result.upserted_id
                else None
            )
        }

    except PyMongoError as error:

        raise RuntimeError(
            f"Unable to seed disease data: {error}"
        ) from error


# ---------------------------------------------------------
# Save anonymous prediction
# ---------------------------------------------------------

def save_prediction(
    district,
    taluka,
    crop,
    model_label,
    confidence,
    risk,
    weather=None,
    report_type="ai_prediction",
    language="en"
):
    """
    Save an anonymous crop-health prediction.

    IMPORTANT:
    This function intentionally does NOT store:

    - farmer name
    - phone number
    - email
    - exact farm address
    - uploaded image

    Only aggregated/location-level information is stored.
    """

    if not district:
        raise ValueError("District is required.")

    if not crop:
        raise ValueError("Crop is required.")

    if not model_label:
        raise ValueError("Model label is required.")

    try:

        collection = get_history_collection()

        prediction_document = {
            "created_at": datetime.now(timezone.utc),

            "district": district,

            "taluka": taluka,

            "crop": crop,

            "model_label": model_label,

            "confidence": float(confidence),

            "risk": {
                "score": int(risk.get("score", 0)),
                "level": risk.get("level", "unknown")
            },

            "weather": weather or {},

            "report_type": report_type,

            "language": language
        }

        result = collection.insert_one(
            prediction_document
        )

        return str(result.inserted_id)

    except (TypeError, ValueError) as error:

        raise ValueError(
            f"Invalid prediction data: {error}"
        ) from error

    except PyMongoError as error:

        raise RuntimeError(
            f"Unable to save prediction: {error}"
        ) from error


# ---------------------------------------------------------
# Regional dashboard summary
# ---------------------------------------------------------

def get_prediction_summary():
    """
    Aggregate anonymous prediction history.

    Results are grouped by:

        district
        crop
        risk level

    Example result:

        {
            "district": "Nagpur",
            "crop": "Tomato",
            "level": "high",
            "count": 12
        }
    """

    try:

        collection = get_history_collection()

        pipeline = [

            {
                "$group": {
                    "_id": {
                        "district": "$district",
                        "crop": "$crop",
                        "level": "$risk.level"
                    },

                    "count": {
                        "$sum": 1
                    },

                    "average_confidence": {
                        "$avg": "$confidence"
                    },

                    "average_risk_score": {
                        "$avg": "$risk.score"
                    }
                }
            },

            {
                "$sort": {
                    "count": -1
                }
            }
        ]

        results = list(
            collection.aggregate(pipeline)
        )

        summary = []

        for item in results:

            group = item.get("_id", {})

            summary.append(
                {
                    "district": group.get(
                        "district",
                        "Unknown"
                    ),

                    "crop": group.get(
                        "crop",
                        "Unknown"
                    ),

                    "level": group.get(
                        "level",
                        "unknown"
                    ),

                    "count": item.get(
                        "count",
                        0
                    ),

                    "average_confidence": round(
                        float(
                            item.get(
                                "average_confidence",
                                0
                            )
                        ),
                        3
                    ),

                    "average_risk_score": round(
                        float(
                            item.get(
                                "average_risk_score",
                                0
                            )
                        ),
                        2
                    )
                }
            )

        return summary

    except PyMongoError as error:

        raise RuntimeError(
            f"Unable to generate regional summary: {error}"
        ) from error


# ---------------------------------------------------------
# District-level summary
# ---------------------------------------------------------

def get_district_summary(district):
    """
    Return prediction statistics for one district.
    """

    if not district:
        return []

    try:

        collection = get_history_collection()

        pipeline = [

            {
                "$match": {
                    "district": district
                }
            },

            {
                "$group": {
                    "_id": {
                        "crop": "$crop",
                        "level": "$risk.level"
                    },

                    "count": {
                        "$sum": 1
                    },

                    "average_confidence": {
                        "$avg": "$confidence"
                    },

                    "average_risk_score": {
                        "$avg": "$risk.score"
                    }
                }
            },

            {
                "$sort": {
                    "count": -1
                }
            }
        ]

        results = list(
            collection.aggregate(pipeline)
        )

        summary = []

        for item in results:

            group = item.get("_id", {})

            summary.append(
                {
                    "district": district,

                    "crop": group.get(
                        "crop",
                        "Unknown"
                    ),

                    "level": group.get(
                        "level",
                        "unknown"
                    ),

                    "count": item.get(
                        "count",
                        0
                    ),

                    "average_confidence": round(
                        float(
                            item.get(
                                "average_confidence",
                                0
                            )
                        ),
                        3
                    ),

                    "average_risk_score": round(
                        float(
                            item.get(
                                "average_risk_score",
                                0
                            )
                        ),
                        2
                    )
                }
            )

        return summary

    except PyMongoError as error:

        raise RuntimeError(
            f"Unable to generate district summary: {error}"
        ) from error