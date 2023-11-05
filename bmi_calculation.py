from constants import WEIGHT, HEIGHT

def calculate_bmi_for_regular_build(data):
    """
    Calculate BMI and determine the condition for individuals with a regular build.

    Calculates the Body Mass Index (BMI) for individuals with a regular build based
    on their Height (meters)  and weight. It then determines their condition (Underweight, Normal,
    Overweight, or Obese) based on the BMI value.

    Args:
    data (list of dict): A list of dictionaries, each containing patient information,
        including Height (meters)  and weight.

    Returns:
    list of dict: A list of dictionaries, with each dictionary containing the calculated
        BMI, build type ('Regular'), and condition (Underweight, Normal, Overweight, or Obese).
    """
    return [
        {
            'Build': 'Regular',
            'BMI': float(value[WEIGHT]) / (float(value[HEIGHT]) ** 2),
            'Condition': 'Underweight' if float(value[WEIGHT]) / (float(value[HEIGHT]) ** 2) < 18.5
            else 'Normal' if float(value[WEIGHT]) / (float(value[HEIGHT]) ** 2) < 25
            else 'Overweight' if float(value[WEIGHT]) / (float(value[HEIGHT]) ** 2) < 29
            else 'Obese'
        }
        for value in data
    ]


def calculate_bmi_for_athletic_build(data):
    """
    Calculate BMI and determine the condition for individuals with an athletic build.

    Calculates the Body Mass Index (BMI) for individuals with an athletic build based
    on their Height (meters)  and weight. It then determines their condition (Underweight, Normal,
    Overweight, or Obese) based on the BMI value.

    Args:
    data (list of dict): A list of dictionaries, each containing patient information,
        including Height (meters)  and weight.

    Returns:
    list of dict: A list of dictionaries, with each dictionary containing the calculated
        BMI, build type ('Athletic'), and condition (Underweight, Normal, Overweight, or Obese).
    """
    return [
        {
            'Build': 'Athletic',
            'BMI': float(value[WEIGHT]) / (float(value[HEIGHT]) ** 2),
            'Condition': 'Underweight' if float(value[WEIGHT]) / (float(value[HEIGHT]) ** 2) < 18.5
            else 'Normal' if float(value[WEIGHT]) / (float(value[HEIGHT]) ** 2) < 25
            else 'Overweight' if float(value[WEIGHT]) / (float(value[HEIGHT]) ** 2) < 30
            else 'Obese'
        }
        for value in data
    ]


def calculate_bmi_for_slim_build(data):
    """
    Calculate BMI and determine the condition for individuals with a slim build.

    Calculates the Body Mass Index (BMI) for individuals with a slim build based
    on their Height (meters)  and weight. It then determines their condition (Underweight, Normal,
    Overweight, or Obese) based on the BMI value.

    Args:
    data (list of dict): A list of dictionaries, each containing patient information,
        including Height (meters)  and weight.

    Returns:
    list of dict: A list of dictionaries, with each dictionary containing the calculated
        BMI, build type ('Slim'), and condition (Underweight, Normal, Overweight, or Obese).
    """
    return [
        {
            'Build': 'Slim',
            'BMI': float(value[WEIGHT]) / (float(value[HEIGHT]) ** 2),
            'Condition': 'Underweight' if float(value[WEIGHT]) / (float(value[HEIGHT]) ** 2) < 18.5
            else 'Normal' if float(value[WEIGHT]) / (float(value[HEIGHT]) ** 2) < 25
            else 'Overweight' if float(value[WEIGHT]) / (float(value[HEIGHT]) ** 2) < 28
            else 'Obese'
        }
        for value in data
    ]
