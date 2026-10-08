# services/dosage_service.py

"""
Dosage calculation service for Smart Agri AI.

IMPORTANT SAFETY RULE:

This service does NOT recommend pesticide dosage.

The user must provide a verified product-label rate.

The calculator only performs arithmetic using that
verified value and the farm area.

Example:

    Label rate = 20 ml per pump
    Farm area = 2 acres
    Pumps per acre = 10

    Total pumps = 2 * 10 = 20 pumps
    Total product = 20 * 20 = 400 ml

Never use an AI-generated dosage as a replacement
for an approved product label.
"""


# ---------------------------------------------------------
# VALIDATION
# ---------------------------------------------------------

def _validate_non_negative(
    value,
    field_name
):
    """
    Validate that a numeric value is not negative.
    """

    try:
        value = float(value)

    except (TypeError, ValueError) as error:

        raise ValueError(
            f"{field_name} must be a valid number."
        ) from error

    if value < 0:

        raise ValueError(
            f"{field_name} cannot be negative."
        )

    return value


# ---------------------------------------------------------
# TOTAL PUMPS
# ---------------------------------------------------------

def calculate_total_pumps(
    pumps_per_acre,
    farm_area
):
    """
    Calculate the total number of pumps required.

    Formula:

        total pumps =
            pumps per acre × farm area

    Example:

        10 pumps/acre × 2 acres = 20 pumps
    """

    pumps_per_acre = _validate_non_negative(
        pumps_per_acre,
        "Pumps per acre"
    )

    farm_area = _validate_non_negative(
        farm_area,
        "Farm area"
    )

    return pumps_per_acre * farm_area


# ---------------------------------------------------------
# TOTAL PRODUCT
# ---------------------------------------------------------

def calculate_total_quantity(
    quantity_per_pump,
    pumps_per_acre,
    farm_area
):
    """
    Calculate the total product quantity.

    Formula:

        total quantity =
            quantity per pump
            × pumps per acre
            × farm area

    The quantity_per_pump MUST come from the
    approved product label.
    """

    quantity_per_pump = _validate_non_negative(
        quantity_per_pump,
        "Label quantity per pump"
    )

    total_pumps = calculate_total_pumps(
        pumps_per_acre,
        farm_area
    )

    return quantity_per_pump * total_pumps


# ---------------------------------------------------------
# COMPLETE DOSAGE CALCULATION
# ---------------------------------------------------------

def calculate_product_quantity(
    quantity_per_pump,
    pumps_per_acre,
    farm_area,
    unit="ml"
):
    """
    Return a complete transparent calculation.

    This makes it easier for the UI to show the farmer
    exactly how the final quantity was calculated.

    Returns:

        {
            "farm_area": 2,
            "pumps_per_acre": 10,
            "total_pumps": 20,
            "quantity_per_pump": 20,
            "total_quantity": 400,
            "unit": "ml"
        }
    """

    quantity_per_pump = _validate_non_negative(
        quantity_per_pump,
        "Label quantity per pump"
    )

    pumps_per_acre = _validate_non_negative(
        pumps_per_acre,
        "Pumps per acre"
    )

    farm_area = _validate_non_negative(
        farm_area,
        "Farm area"
    )

    if not unit or not str(unit).strip():

        raise ValueError(
            "Product unit cannot be empty."
        )

    total_pumps = calculate_total_pumps(
        pumps_per_acre,
        farm_area
    )

    total_quantity = (
        quantity_per_pump
        * total_pumps
    )

    return {
        "farm_area": farm_area,
        "pumps_per_acre": pumps_per_acre,
        "total_pumps": total_pumps,
        "quantity_per_pump": quantity_per_pump,
        "total_quantity": total_quantity,
        "unit": str(unit).strip()
    }