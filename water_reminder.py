# water_reminder.py

def calculate_water_intake(weight, age): 
    try: 
        weight = float(weight) 
        age = int(age) 
        if weight <= 0 or age <= 0: 
            raise ValueError("Weight and age must be positive numbers.") 
    except ValueError as ve: 
        return f"Invalid input: {ve}" 
    
    water_intake = weight * 0.033 
    if age < 18: 
        reminder = "Every 3 hours" 
    elif age < 50: 
        reminder = "Every 2 hours" 
    else: 
        reminder = "Every 1.5 hours" 

    return f"Recommended water intake: {water_intake:.2f} L/day | Reminder: {reminder}"


# Test run
if __name__ == "__main__":
    print(calculate_water_intake(70, 25))          # Valid input
    print(calculate_water_intake("abc", 25))       # Invalid weight
    print(calculate_water_intake(60, -10))         # Negative age
    print(calculate_water_intake(55, 65))          # Elderly person
