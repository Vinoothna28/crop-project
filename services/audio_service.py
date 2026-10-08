# services/audio_service.py

"""
Audio service for Smart Agri AI.

Uses gTTS (Google Text-to-Speech) to convert localized
agricultural recommendations and warnings into MP3 files.

Supported languages:
    en -> English
    te -> Telugu
    hi -> Hindi

The generated file path can be passed directly to
Streamlit's st.audio().
"""

import hashlib
from pathlib import Path

from gtts import gTTS
from gtts.tts import gTTSError


# ---------------------------------------------------------
# Audio directory
# ---------------------------------------------------------

AUDIO_DIRECTORY = Path("assets/audio")


# ---------------------------------------------------------
# Language mapping
# ---------------------------------------------------------

GTTS_LANGUAGES = {
    "en": "en",
    "te": "te",
    "hi": "hi"
}


# ---------------------------------------------------------
# Language normalization
# ---------------------------------------------------------

def normalize_audio_language(language):
    """
    Convert a language name/code into the language code
    expected by gTTS.

    Examples:
        English -> en
        Telugu  -> te
        Hindi   -> hi
    """

    if not language:
        return "en"

    language = str(language).strip()

    language_map = {
        "English": "en",
        "Telugu": "te",
        "Hindi": "hi"
    }

    if language in language_map:
        return language_map[language]

    language = language.lower()

    if language in GTTS_LANGUAGES:
        return language

    return "en"


# ---------------------------------------------------------
# Generate audio
# ---------------------------------------------------------

def generate_audio(text, language="en"):
    """
    Convert text into an MP3 audio file.

    Parameters:
        text:
            Localized recommendation, warning or advisory.

        language:
            English, Telugu, Hindi or en/te/hi.

    Returns:
        Path to the generated MP3 file.

    Raises:
        ValueError:
            When text is empty or language is unsupported.

        RuntimeError:
            When gTTS or the network fails.
    """

    if not text or not str(text).strip():
        raise ValueError(
            "Audio text cannot be empty."
        )

    language_code = normalize_audio_language(language)

    if language_code not in GTTS_LANGUAGES:
        raise ValueError(
            f"Unsupported audio language: {language}"
        )

    try:

        # Create audio directory if it doesn't exist.
        AUDIO_DIRECTORY.mkdir(
            parents=True,
            exist_ok=True
        )

        clean_text = str(text).strip()

        # Create a deterministic filename.
        #
        # Same text + same language =
        # same file, so we don't repeatedly call gTTS.
        text_hash = hashlib.sha256(
            f"{language_code}:{clean_text}".encode("utf-8")
        ).hexdigest()[:16]

        output_file = (
            AUDIO_DIRECTORY
            / f"{language_code}_{text_hash}.mp3"
        )

        # Reuse existing audio file.
        if output_file.exists():
            return str(output_file)

        # Generate speech.
        tts = gTTS(
            text=clean_text,
            lang=GTTS_LANGUAGES[language_code],
            slow=False
        )

        tts.save(
            str(output_file)
        )

        return str(output_file)

    except gTTSError as error:

        raise RuntimeError(
            "Text-to-speech service failed. "
            "Please check your internet connection "
            "and try again."
        ) from error

    except OSError as error:

        raise RuntimeError(
            "Unable to save the generated audio file."
        ) from error

    except Exception as error:

        raise RuntimeError(
            f"Unexpected audio generation error: {error}"
        ) from error


# ---------------------------------------------------------
# Safe audio generation
# ---------------------------------------------------------

def try_generate_audio(text, language="en"):
    """
    Generate audio without allowing an audio failure to
    break the main application.

    Returns:
        file path if successful
        None if audio generation fails
    """

    try:

        return generate_audio(
            text=text,
            language=language
        )

    except (ValueError, RuntimeError):

        return None