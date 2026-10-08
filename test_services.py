from pathlib import Path

from services.weather_service import get_weather_for_location
from services.mongo_service import get_database
from services.hf_service import try_classify_image
from services.risk_engine import (
    calculate_risk,
    evaluate_early_warning
)
from services.localization import (
    SUPPORTED_LANGUAGES,
    t
)


def print_title(title):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)


def print_success(message):
    print(f"[PASS] {message}")


def print_failure(message):
    print(f"[FAIL] {message}")


# ---------------------------------------------------------
# 1. WEATHER SERVICE TEST
# ---------------------------------------------------------

def test_weather_service():
    print_title("TEST 1 - WEATHER SERVICE")

    district = "Nashik"

    try:
        print(f"Testing location: {district}")

        result = get_weather_for_location(district)

        location = result["location"]
        weather = result["weather"]

        print("\nGeocoded Location:")
        print(f"Name        : {location['name']}")
        print(f"Latitude    : {location['latitude']}")
        print(f"Longitude   : {location['longitude']}")
        print(f"Country     : {location['country']}")

        print("\nCurrent Weather:")
        print(f"Temperature : {weather['temperature_c']} °C")
        print(f"Humidity    : {weather['relative_humidity']} %")
        print(f"Rainfall    : {weather['precipitation_mm']} mm")
        print(f"Weather Code: {weather['weather_code']}")

        if (
            weather["temperature_c"] is not None
            and weather["relative_humidity"] is not None
        ):
            print_success(
                "Weather service is working correctly."
            )
            return True

        print_failure(
            "Weather response is missing temperature or humidity."
        )
        return False

    except Exception as error:
        print_failure(
            f"Weather service failed: {error}"
        )
        return False


# ---------------------------------------------------------
# 2. MONGODB ATLAS TEST
# ---------------------------------------------------------

def test_mongodb():
    print_title("TEST 2 - MONGODB ATLAS")

    try:
        print("Connecting to MongoDB Atlas...")

        database = get_database()

        print_success(
            f"Connected to database: {database.name}"
        )

        test_collection = database["service_tests"]

        test_document = {
            "test_type": "microservice_test",
            "service": "mongodb",
            "status": "passed",
            "message": "MongoDB connection test"
        }

        insert_result = test_collection.insert_one(
            test_document
        )

        print(
            f"Inserted document ID: {insert_result.inserted_id}"
        )

        saved_document = test_collection.find_one(
            {"_id": insert_result.inserted_id}
        )

        if saved_document:
            print_success(
                "MongoDB write and read test passed."
            )

            test_collection.delete_one(
                {"_id": insert_result.inserted_id}
            )

            print_success(
                "Temporary test document deleted."
            )

            return True

        print_failure(
            "Document was inserted but could not be read."
        )
        return False

    except Exception as error:
        print_failure(
            f"MongoDB test failed: {error}"
        )
        return False


# ---------------------------------------------------------
# 3. HUGGING FACE TEST
# ---------------------------------------------------------

def test_huggingface():
    print_title("TEST 3 - HUGGING FACE AI SERVICE")

    image_folder = Path("test_images")

    if not image_folder.exists():
        print_failure(
            "test_images folder does not exist."
        )

        print(
            "\nCreate this folder:"
        )

        print(
            "test_images/"
        )

        print(
            "and place one crop/leaf image inside it."
        )

        return False

    image_files = [
        file
        for file in image_folder.iterdir()
        if file.suffix.lower()
        in [".jpg", ".jpeg", ".png", ".webp"]
    ]

    if not image_files:
        print_failure(
            "No test image found inside test_images/"
        )

        print(
            "\nPlace a leaf image inside:"
        )

        print(
            "test_images/sample.jpg"
        )

        return False

    image_path = image_files[0]

    print(f"Testing image: {image_path}")

    try:
        image_bytes = image_path.read_bytes()

        result = try_classify_image(
            image_bytes=image_bytes,
            top_k=5
        )

        if not result["success"]:
            print_failure(
                f"HF service failed: {result['error']}"
            )
            return False

        predictions = result["predictions"]

        if not predictions:
            print_failure(
                "HF returned no predictions."
            )
            return False

        print("\nAI Predictions:")

        for index, prediction in enumerate(
            predictions,
            start=1
        ):
            label = prediction["label"]
            confidence = prediction["score"]

            print(
                f"{index}. "
                f"{label} "
                f"-> {confidence:.2%}"
            )

        top_prediction = predictions[0]

        if (
            isinstance(top_prediction["label"], str)
            and 0 <= top_prediction["score"] <= 1
        ):
            print_success(
                "Hugging Face AI service returned valid predictions."
            )
            return True

        print_failure(
            "HF returned an invalid label or confidence score."
        )
        return False

    except Exception as error:
        print_failure(
            f"Hugging Face test failed: {error}"
        )
        return False


# ---------------------------------------------------------
# 4. RISK ENGINE TEST
# ---------------------------------------------------------

def test_risk_engine():
    print_title("TEST 4 - RISK ENGINE")

    try:
        temperature = 25
        humidity = 85
        severity = 45
        confidence = 0.90

        disease_profile = {
            "min_temp_c": 20,
            "max_temp_c": 30,
            "min_humidity": 75
        }

        print(f"Temperature : {temperature} °C")
        print(f"Humidity    : {humidity} %")
        print(f"Severity    : {severity}")
        print(f"Confidence  : {confidence:.0%}")

        result = calculate_risk(
            temperature_c=temperature,
            humidity=humidity,
            severity=severity,
            profile=disease_profile,
            confidence=confidence
        )

        print("\nRisk Result:")
        print(f"Risk Score       : {result['score']}")
        print(f"Risk Level       : {result['level']}")
        print(f"Severity Score   : {result['severity_score']}")
        print(
            f"Environment Score: "
            f"{result['environment_score']}"
        )
        print(
            f"Confidence Level : "
            f"{result['confidence_level']}"
        )
        print(
            f"Weather Favorable: "
            f"{result['weather_favorable']}"
        )

        print("\nRisk Reasons:")

        for reason in result["reasons"]:
            print(f"- {reason}")

        warning = evaluate_early_warning(
            severity=severity,
            weather_favorable=result["weather_favorable"],
            risk_score=result["score"],
            confidence=confidence
        )

        print("\nEarly Warning:")
        print(f"Triggered : {warning['triggered']}")
        print(f"Level     : {warning['level']}")
        print(f"Message   : {warning['advisory']}")

        if 0 <= result["score"] <= 100:
            print_success(
                "Risk engine is working correctly."
            )
            return True

        print_failure(
            "Risk score is outside the expected range."
        )
        return False

    except Exception as error:
        print_failure(
            f"Risk engine test failed: {error}"
        )
        return False


# ---------------------------------------------------------
# 5. LOCALIZATION TEST
# ---------------------------------------------------------

def test_localization():
    print_title("TEST 5 - LOCALIZATION")

    try:
        print("Supported languages:")
        print(SUPPORTED_LANGUAGES)

        test_key = "weather"

        for language in [
            "English",
            "Telugu",
            "Hindi"
        ]:
            translated_text = t(
                test_key,
                language
            )

            print(
                f"{language:10} -> {translated_text}"
            )

            if not translated_text:
                print_failure(
                    f"Missing translation for {language}"
                )
                return False

        print_success(
            "Localization is working for "
            "English, Telugu and Hindi."
        )

        return True

    except Exception as error:
        print_failure(
            f"Localization test failed: {error}"
        )
        return False


# ---------------------------------------------------------
# FINAL SUMMARY
# ---------------------------------------------------------

def main():
    print("\n")
    print("*" * 60)
    print("SMART AGRI AI - MICROSERVICE TEST SUITE")
    print("*" * 60)

    results = {}

    results["Weather"] = test_weather_service()

    results["MongoDB"] = test_mongodb()

    results["Hugging Face"] = test_huggingface()

    results["Risk Engine"] = test_risk_engine()

    results["Localization"] = test_localization()

    print_title("FINAL TEST SUMMARY")

    passed = 0
    failed = 0

    for service, status in results.items():

        if status:
            print(f"[PASS] {service}")
            passed += 1
        else:
            print(f"[FAIL] {service}")
            failed += 1

    print("\n" + "-" * 60)

    print(f"Passed: {passed}")
    print(f"Failed: {failed}")

    print("-" * 60)

    if failed == 0:
        print(
            "\nALL MICROSERVICE TESTS PASSED."
        )

        print(
            "The project is ready for the "
            "end-to-end simulation."
        )

    else:
        print(
            "\nSOME TESTS FAILED."
        )

        print(
            "Fix the failed service before "
            "running the full application."
        )


if __name__ == "__main__":
    main()