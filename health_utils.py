def calculate_bmi(height, weight):
    """
    Calculate Body Mass Index (BMI) given height in meters and weight in kilograms.
    
    Args:
        height (float): Height in meters
        weight (float): Weight in kilograms
        
    Returns:
        float: BMI value
    """
    if height <= 0 or weight <= 0:
        raise ValueError("Height and weight must be positive numbers")
    
    return weight / (height ** 2)

def calculate_bmr(height, weight, age, gender):
    """
    Calculate Basal Metabolic Rate (BMR) using the Harris-Benedict equation.
    
    Args:
        height (float): Height in centimeters
        weight (float): Weight in kilograms
        age (int): Age in years
        gender (str): Either 'male' or 'female'
        
    Returns:
        float: BMR value
    """
    if height <= 0 or weight <= 0 or age <= 0:
        raise ValueError("Height, weight and age must be positive numbers")
    
    gender = gender.lower()
    if gender not in ['male', 'female']:
        raise ValueError("Gender must be either 'male' or 'female'")
    
    if gender == 'male':
        return 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    else: 
        return 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)