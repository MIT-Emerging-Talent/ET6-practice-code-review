def calculate_water_intake(weight, activity_level, climate):
    """
    Calculates the daily water intake recommendation (in liters) based on:
    - Weight (in kg)
    - Activity level (Low, Moderate, High)
    - Climate (Cold, Temperate, Hot)
    
    Raises:
        ValueError: If inputs are invalid.
    """
    # Validate weight
    if weight <= 0:
        raise ValueError("Weight must be a positive number.")

    # Base water intake (liters per kg of body weight)
    base_intake = weight * 0.033  # Standard recommendation

    # Activity level adjustment
    activity_factors = {
        "Low": 0,
        "Moderate": 0.5,
        "High": 1.0
    }

    if activity_level not in activity_factors:
        raise ValueError(f"Invalid activity level: {activity_level}. Choose 'Low', 'Moderate', or 'High'.")

    activity_adjustment = activity_factors[activity_level]

    # Climate adjustment
    climate_factors = {
        "Cold": -0.2,
        "Temperate": 0,
        "Hot": 0.5
    }

    if climate not in climate_factors:
        raise ValueError(f"Invalid climate: {climate}. Choose 'Cold', 'Temperate', or 'Hot'.")

    climate_adjustment = climate_factors[climate]

    # Calculate total water intake
    total_intake = base_intake + activity_adjustment + climate_adjustment
    return round(total_intake, 2)  # Rounded to 2 decimal places
