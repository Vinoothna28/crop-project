# services/risk_engine.py

"""
Risk engine for Smart Agri AI.

The risk engine combines:

1. Disease severity
2. Current temperature
3. Current humidity
4. AI prediction confidence

to produce a simple crop-health risk indicator:

    Low
    Moderate
    High

IMPORTANT:

The disease profiles and thresholds used by this project
are configuration values for the prototype. They are not
validated epidemiological outbreak thresholds.

Therefore, the result must be presented as an advisory
risk indicator and NOT as a confirmed disease outbreak.
"""


# ---------------------------------------------------------
# ENVIRONMENT SCORE
# ---------------------------------------------------------

def calculate_environment_score(
    temperature_c,
    humidity,
    profile
):
    """
    Calculate environmental risk contribution.

    Maximum environmental contribution = 50 points.

    Temperature:
        +25 points when temperature is inside the
        configured disease-risk range.

    Humidity:
        +25 points when humidity is equal to or above
        the configured minimum humidity.

    Returns:

        (
            environment_score,
            reasons,
            weather_favorable
        )
    """

    if not isinstance(profile, dict):
        raise ValueError(
            "Disease risk profile must be a dictionary."
        )

    score = 0

    reasons = []

    temperature_favorable = False
    humidity_favorable = False

    # -----------------------------------------------------
    # Read configured thresholds
    # -----------------------------------------------------

    min_temp = profile.get(
        "min_temp_c"
    )

    max_temp = profile.get(
        "max_temp_c"
    )

    min_humidity = profile.get(
        "min_humidity"
    )

    # -----------------------------------------------------
    # Temperature check
    # -----------------------------------------------------

    if temperature_c is not None:

        try:
            temperature_c = float(
                temperature_c
            )

        except (TypeError, ValueError):

            temperature_c = None

    if (
        temperature_c is not None
        and min_temp is not None
        and max_temp is not None
    ):

        try:

            min_temp = float(min_temp)
            max_temp = float(max_temp)

            temperature_favorable = (
                min_temp
                <= temperature_c
                <= max_temp
            )

        except (TypeError, ValueError):

            temperature_favorable = False

    if temperature_favorable:

        score += 25

        reasons.append(
            "Temperature is within the "
            "configured risk range."
        )

    # -----------------------------------------------------
    # Humidity check
    # -----------------------------------------------------

    if humidity is not None:

        try:
            humidity = float(humidity)

        except (TypeError, ValueError):

            humidity = None

    if (
        humidity is not None
        and min_humidity is not None
    ):

        try:

            min_humidity = float(
                min_humidity
            )

            humidity_favorable = (
                humidity >= min_humidity
            )

        except (TypeError, ValueError):

            humidity_favorable = False

    if humidity_favorable:

        score += 25

        reasons.append(
            "Humidity is at or above the "
            "configured risk threshold."
        )

    # -----------------------------------------------------
    # Overall environmental condition
    # -----------------------------------------------------

    weather_favorable = (
        temperature_favorable
        and humidity_favorable
    )

    if not reasons:

        reasons.append(
            "Current weather conditions do not "
            "match the configured environmental "
            "risk conditions."
        )

    return (
        min(score, 50),
        reasons,
        weather_favorable
    )


# ---------------------------------------------------------
# CONFIDENCE CATEGORY
# ---------------------------------------------------------

def get_confidence_level(
    confidence,
    high_threshold=0.80,
    medium_threshold=0.60
):
    """
    Convert model confidence into a readable category.

    Example:

        >= 0.80 -> high
        >= 0.60 -> moderate
        <  0.60 -> low
    """

    try:

        confidence = float(
            confidence
        )

    except (TypeError, ValueError) as error:

        raise ValueError(
            "Prediction confidence must be a number."
        ) from error

    # Support accidental percentage input such as 85.
    if confidence > 1:

        confidence = confidence / 100

    confidence = max(
        0.0,
        min(confidence, 1.0)
    )

    if confidence >= high_threshold:

        return "high"

    if confidence >= medium_threshold:

        return "moderate"

    return "low"


# ---------------------------------------------------------
# MAIN RISK CALCULATION
# ---------------------------------------------------------

def calculate_risk(
    temperature_c,
    humidity,
    severity,
    profile,
    confidence=0.0
):
    """
    Calculate the combined crop-health risk.

    Components:

        Environmental score: 0 - 50
        Disease severity:    0 - 50

    Total risk score:

        0 - 100

    Confidence does NOT blindly increase the disease risk.

    Instead, confidence is used to determine whether a
    high-risk prediction is reliable enough to generate
    an early warning.

    Returns a dictionary containing:

        score
        level
        severity_score
        environment_score
        confidence
        confidence_level
        weather_favorable
        reasons
    """

    # -----------------------------------------------------
    # Validate severity
    # -----------------------------------------------------

    try:

        severity = float(
            severity
        )

    except (TypeError, ValueError) as error:

        raise ValueError(
            "Disease severity must be a number."
        ) from error

    severity_score = int(
        max(
            0,
            min(severity, 50)
        )
    )

    # -----------------------------------------------------
    # Normalize confidence
    # -----------------------------------------------------

    try:

        confidence = float(
            confidence
        )

    except (TypeError, ValueError) as error:

        raise ValueError(
            "Prediction confidence must be a number."
        ) from error

    if confidence > 1:

        confidence = confidence / 100

    confidence = max(
        0.0,
        min(confidence, 1.0)
    )

    # -----------------------------------------------------
    # Environmental score
    # -----------------------------------------------------

    (
        environment_score,
        reasons,
        weather_favorable
    ) = calculate_environment_score(
        temperature_c,
        humidity,
        profile
    )

    # -----------------------------------------------------
    # Combined score
    # -----------------------------------------------------

    total_score = (
        severity_score
        + environment_score
    )

    total_score = max(
        0,
        min(total_score, 100)
    )

    # -----------------------------------------------------
    # Risk level
    # -----------------------------------------------------

    if total_score >= 75:

        level = "high"

    elif total_score >= 40:

        level = "moderate"

    else:

        level = "low"

    # -----------------------------------------------------
    # Confidence category
    # -----------------------------------------------------

    confidence_level = get_confidence_level(
        confidence
    )

    return {
        "score": int(total_score),
        "level": level,
        "severity_score": severity_score,
        "environment_score": environment_score,
        "confidence": round(
            confidence,
            3
        ),
        "confidence_level": confidence_level,
        "weather_favorable": weather_favorable,
        "reasons": reasons
    }


# ---------------------------------------------------------
# EARLY WARNING
# ---------------------------------------------------------

def should_trigger_warning(
    severity,
    weather_favorable,
    risk_score,
    confidence,
    confidence_threshold=0.70
):
    """
    Determine whether an early warning should be displayed.

    A warning is triggered only when ALL important conditions
    are satisfied:

        1. Disease severity is significant.
        2. Weather conditions are favorable.
        3. Combined risk score is high.
        4. Model confidence is sufficiently high.

    This does NOT confirm an outbreak.

    It only indicates elevated risk based on the available
    image prediction and environmental information.
    """

    try:

        severity = float(
            severity
        )

        risk_score = float(
            risk_score
        )

        confidence = float(
            confidence
        )

    except (TypeError, ValueError):

        return False

    if confidence > 1:

        confidence = confidence / 100

    confidence = max(
        0.0,
        min(confidence, 1.0)
    )

    return (
        severity >= 40
        and weather_favorable is True
        and risk_score >= 75
        and confidence >= confidence_threshold
    )


# ---------------------------------------------------------
# COMPLETE WARNING RESULT
# ---------------------------------------------------------

def evaluate_early_warning(
    severity,
    weather_favorable,
    risk_score,
    confidence,
    confidence_threshold=0.70
):
    """
    Return a structured early-warning result.

    This is useful for the UI because it avoids putting
    warning logic directly inside app.py.
    """

    warning = should_trigger_warning(
        severity=severity,
        weather_favorable=weather_favorable,
        risk_score=risk_score,
        confidence=confidence,
        confidence_threshold=confidence_threshold
    )

    if warning:

        return {
            "triggered": True,
            "level": "high",
            "message_type": "emergency_risk_warning",
            "advisory": (
                "Available image, confidence and "
                "environmental conditions indicate "
                "elevated crop-health risk. "
                "This is an advisory indicator, "
                "not a confirmed outbreak."
            )
        }

    return {
        "triggered": False,
        "level": "normal",
        "message_type": "no_emergency",
        "advisory": (
            "No elevated emergency risk was detected "
            "from the available information."
        )
    }