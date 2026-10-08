# services/weather_service.py

"""
Weather service for Smart Agri AI.

Uses Open-Meteo APIs to:

1. Convert a location name into latitude and longitude.
2. Fetch current temperature and relative humidity.

Open-Meteo does not require an API key for the basic API.

The service is intentionally separated from the UI so that
weather functionality can be reused by the risk engine,
dashboard, and advisory modules.
"""

import requests


# ---------------------------------------------------------
# API ENDPOINTS
# ---------------------------------------------------------

GEOCODING_URL = (
    "https://geocoding-api.open-meteo.com/v1/search"
)

WEATHER_URL = (
    "https://api.open-meteo.com/v1/forecast"
)


# ---------------------------------------------------------
# CONFIGURATION
# ---------------------------------------------------------

REQUEST_TIMEOUT = 10


# ---------------------------------------------------------
# GEOCODING
# ---------------------------------------------------------

def geocode_location(location_name):
    """
    Convert a location name into geographical coordinates.

    Example:

        geocode_location("Nagpur")

    Returns:

        {
            "name": "Nagpur",
            "latitude": ...,
            "longitude": ...,
            "country": "India",
            "admin1": "Maharashtra",
            "timezone": ...
        }

    Raises:
        ValueError
            If the location is empty or not found.

        ConnectionError
            If Open-Meteo cannot be reached.

        RuntimeError
            For unexpected API or response errors.
    """

    if not location_name or not str(location_name).strip():
        raise ValueError(
            "Location name cannot be empty."
        )

    location_name = str(location_name).strip()

    params = {
        "name": location_name,
        "count": 1,
        "language": "en",
        "format": "json",
        "countryCode": "IN"
    }

    try:

        response = requests.get(
            GEOCODING_URL,
            params=params,
            timeout=REQUEST_TIMEOUT
        )

        response.raise_for_status()

    except requests.exceptions.Timeout as error:

        raise ConnectionError(
            "Weather location service timed out. "
            "Please try again."
        ) from error

    except requests.exceptions.ConnectionError as error:

        raise ConnectionError(
            "Unable to connect to the weather service. "
            "Please check your internet connection."
        ) from error

    except requests.exceptions.HTTPError as error:

        raise RuntimeError(
            "Weather location service returned an error."
        ) from error

    except requests.exceptions.RequestException as error:

        raise RuntimeError(
            f"Weather location request failed: {error}"
        ) from error

    try:

        data = response.json()

    except ValueError as error:

        raise RuntimeError(
            "Weather location service returned invalid data."
        ) from error

    results = data.get("results", [])

    if not results:

        raise ValueError(
            f"Location not found: {location_name}"
        )

    result = results[0]

    try:

        return {
            "name": result.get(
                "name",
                location_name
            ),
            "latitude": float(
                result["latitude"]
            ),
            "longitude": float(
                result["longitude"]
            ),
            "country": result.get(
                "country"
            ),
            "admin1": result.get(
                "admin1"
            ),
            "timezone": result.get(
                "timezone"
            )
        }

    except (KeyError, TypeError, ValueError) as error:

        raise RuntimeError(
            "Location data received from the "
            "weather service is incomplete."
        ) from error


# ---------------------------------------------------------
# CURRENT WEATHER
# ---------------------------------------------------------

def get_current_weather(latitude, longitude):
    """
    Fetch current weather conditions.

    Currently retrieves:

        - Temperature at 2 metres
        - Relative humidity at 2 metres
        - Precipitation
        - Weather code
        - Observation/model time
        - Timezone

    Raises:
        ValueError
            If coordinates are invalid.

        ConnectionError
            If the API cannot be reached.

        RuntimeError
            If the API response is invalid.
    """

    try:

        latitude = float(latitude)
        longitude = float(longitude)

    except (TypeError, ValueError) as error:

        raise ValueError(
            "Latitude and longitude must be valid numbers."
        ) from error

    if not -90 <= latitude <= 90:
        raise ValueError(
            "Latitude must be between -90 and 90."
        )

    if not -180 <= longitude <= 180:
        raise ValueError(
            "Longitude must be between -180 and 180."
        )

    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": (
            "temperature_2m,"
            "relative_humidity_2m,"
            "precipitation,"
            "weather_code"
        ),
        "timezone": "auto"
    }

    try:

        response = requests.get(
            WEATHER_URL,
            params=params,
            timeout=REQUEST_TIMEOUT
        )

        response.raise_for_status()

    except requests.exceptions.Timeout as error:

        raise ConnectionError(
            "Weather service timed out. "
            "Please try again."
        ) from error

    except requests.exceptions.ConnectionError as error:

        raise ConnectionError(
            "Unable to connect to the weather service. "
            "Please check your internet connection."
        ) from error

    except requests.exceptions.HTTPError as error:

        raise RuntimeError(
            "Weather service returned an HTTP error."
        ) from error

    except requests.exceptions.RequestException as error:

        raise RuntimeError(
            f"Weather request failed: {error}"
        ) from error

    try:

        data = response.json()

    except ValueError as error:

        raise RuntimeError(
            "Weather service returned invalid JSON."
        ) from error

    current = data.get("current")

    if not isinstance(current, dict):

        raise RuntimeError(
            "Current weather information "
            "is missing from the response."
        )

    temperature = current.get(
        "temperature_2m"
    )

    humidity = current.get(
        "relative_humidity_2m"
    )

    if temperature is None or humidity is None:

        raise RuntimeError(
            "Temperature or humidity information "
            "is missing from the weather response."
        )

    try:

        temperature = float(temperature)
        humidity = float(humidity)

    except (TypeError, ValueError) as error:

        raise RuntimeError(
            "Weather values returned by the API "
            "are not valid numbers."
        ) from error

    return {
        "temperature_c": temperature,
        "relative_humidity": humidity,
        "precipitation_mm": current.get(
            "precipitation"
        ),
        "weather_code": current.get(
            "weather_code"
        ),
        "time": current.get(
            "time"
        ),
        "timezone": data.get(
            "timezone"
        )
    }


# ---------------------------------------------------------
# COMPLETE LOCATION WEATHER
# ---------------------------------------------------------

def get_weather_for_location(location_name):
    """
    Get location coordinates and current weather
    in a single function.

    Example:

        weather = get_weather_for_location("Nagpur")

    Returns:

        {
            "location": {...},
            "weather": {...}
        }
    """

    location = geocode_location(
        location_name
    )

    weather = get_current_weather(
        location["latitude"],
        location["longitude"]
    )

    return {
        "location": location,
        "weather": weather
    }