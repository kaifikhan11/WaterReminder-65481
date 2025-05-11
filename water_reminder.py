def calculate_water_intake(weight, age):
    try:
        weight = float(weight)
        age = int(age)
        if weight <= 0 or age <= 0:
            raise ValueError("Weight and age must be positive numbers.")
    except ValueError as ve:
        return f"Invalid input: {ve}"

    water_intake = weight * 0.033

    # Reminder logic
    if age < 18:
        reminder = "Every 3 hours"
    elif age < 50:
        reminder = "Every 2 hours"
    else:
        reminder = "Every 1.5 hours"

    # New Feature: Water temperature suggestion
    if age < 18:
        temperature = "Cool"
    elif age <= 50:
        temperature = "Room temperature"
    else:
        temperature = "Lukewarm"

    return (
        f"Recommended water intake: {water_intake:.2f} L/day | "
        f"Reminder: {reminder} | Ideal water temperature: {temperature}"
    )
