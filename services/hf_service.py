from huggingface_hub import InferenceClient
from huggingface_hub.utils import HfHubHTTPError

from config import HF_TOKEN, HF_MODEL


DEFAULT_TOP_K = 5
INFERENCE_TIMEOUT = 30


def get_hf_client():
    if not HF_TOKEN:
        raise ValueError(
            "Hugging Face API token is missing. "
            "Please configure HF_TOKEN in your .env file."
        )

    try:
        return InferenceClient(
            provider="hf-inference",
            api_key=HF_TOKEN,
            timeout=INFERENCE_TIMEOUT
        )

    except Exception as error:
        raise RuntimeError(
            "Unable to initialize the Hugging Face inference service."
        ) from error


def validate_image_bytes(image_bytes):
    if image_bytes is None:
        raise ValueError("No image was provided.")

    if not isinstance(
        image_bytes,
        (bytes, bytearray, memoryview)
    ):
        raise ValueError(
            "Image data must be provided as bytes."
        )

    if len(image_bytes) == 0:
        raise ValueError(
            "The uploaded image is empty."
        )


def classify_image(
    image_bytes,
    model=None,
    top_k=DEFAULT_TOP_K
):
    validate_image_bytes(image_bytes)

    selected_model = model if model else HF_MODEL

    if not selected_model:
        raise ValueError(
            "Hugging Face model is not configured. "
            "Set HF_MODEL in your .env file."
        )

    try:
        top_k = int(top_k)

    except (TypeError, ValueError) as error:
        raise ValueError(
            "top_k must be a valid integer."
        ) from error

    if top_k < 1:
        raise ValueError(
            "top_k must be at least 1."
        )

    client = get_hf_client()

    try:
        predictions = client.image_classification(
            image=bytes(image_bytes),
            model=selected_model,
            top_k=top_k
        )

    except HfHubHTTPError as error:
        status_code = getattr(
            error.response,
            "status_code",
            None
        )

        if status_code == 401:
            raise RuntimeError(
                "Hugging Face authentication failed. "
                "Please check your HF_TOKEN."
            ) from error

        if status_code == 403:
            raise RuntimeError(
                "Hugging Face access was denied. "
                "Check the token permissions and model access."
            ) from error

        if status_code == 429:
            raise RuntimeError(
                "Hugging Face inference quota or rate "
                "limit has been reached. "
                "Please try again later."
            ) from error

        if status_code == 503:
            raise RuntimeError(
                "The selected AI model is temporarily "
                "unavailable or is loading. "
                "Please try again shortly."
            ) from error

        raise RuntimeError(
            "Hugging Face returned an error while "
            "analyzing the image."
        ) from error

    except TimeoutError as error:
        raise TimeoutError(
            "The Hugging Face AI image analysis "
            "request timed out. Please try again."
        ) from error

    except ConnectionError as error:
        raise ConnectionError(
            "Unable to connect to the Hugging Face "
            "AI service. Please check your internet connection."
        ) from error

    except Exception as error:
        error_message = str(error).lower()

        if (
            "rate limit" in error_message
            or "too many requests" in error_message
            or "quota" in error_message
        ):
            raise RuntimeError(
                "Hugging Face inference quota or rate "
                "limit has been reached. Please try again later."
            ) from error

        if (
            "loading" in error_message
            or "currently unavailable" in error_message
            or "503" in error_message
        ):
            raise RuntimeError(
                "The selected AI model is temporarily "
                "unavailable. Please try again shortly."
            ) from error

        raise RuntimeError(
            f"AI image analysis failed: {error}"
        ) from error

    if predictions is None:
        raise RuntimeError(
            "The AI service returned no prediction."
        )

    if not isinstance(
        predictions,
        (list, tuple)
    ):
        raise RuntimeError(
            "Unexpected response received from the "
            "AI classification service."
        )

    if len(predictions) == 0:
        raise RuntimeError(
            "The AI service could not classify "
            "the uploaded image."
        )

    results = []

    for prediction in predictions:
        try:
            label = getattr(
                prediction,
                "label",
                None
            )

            score = getattr(
                prediction,
                "score",
                None
            )

            if isinstance(prediction, dict):
                label = prediction.get(
                    "label",
                    label
                )

                score = prediction.get(
                    "score",
                    score
                )

            if not label or score is None:
                continue

            score = float(score)

            score = max(
                0.0,
                min(score, 1.0)
            )

            results.append({
                "label": str(label),
                "score": score
            })

        except (TypeError, ValueError):
            continue

    if not results:
        raise RuntimeError(
            "The AI service returned predictions "
            "in an unsupported format."
        )

    results.sort(
        key=lambda item: item["score"],
        reverse=True
    )

    return results


def get_top_prediction(
    image_bytes,
    model=None
):
    predictions = classify_image(
        image_bytes=image_bytes,
        model=model,
        top_k=1
    )

    return predictions[0]


def try_classify_image(
    image_bytes,
    model=None,
    top_k=DEFAULT_TOP_K
):
    try:
        predictions = classify_image(
            image_bytes=image_bytes,
            model=model,
            top_k=top_k
        )

        return {
            "success": True,
            "predictions": predictions,
            "error": None,
            "error_type": None
        }

    except TimeoutError as error:
        return {
            "success": False,
            "predictions": [],
            "error": str(error),
            "error_type": "timeout"
        }

    except ConnectionError as error:
        return {
            "success": False,
            "predictions": [],
            "error": str(error),
            "error_type": "connection"
        }

    except ValueError as error:
        return {
            "success": False,
            "predictions": [],
            "error": str(error),
            "error_type": "configuration"
        }

    except RuntimeError as error:
        return {
            "success": False,
            "predictions": [],
            "error": str(error),
            "error_type": "service"
        }

    except Exception:
        return {
            "success": False,
            "predictions": [],
            "error": (
                "Unexpected error occurred during "
                "AI image analysis."
            ),
            "error_type": "unknown"
        }