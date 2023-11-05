from datetime import datetime

def calculate_age_from_birthdate(birthdate, current_year=2023):
    """
    Calculate a person's age from their birthdate.

    Calculates a person's age based on their birthdate and the current year.

    Args:
    birthdate (str): The birthdate in the format 'dd/mm/yyyy'.
    current_year (int, optional): The current year. Default is 2023.

    Returns:
    int: The person's age.
    """
    birthdate_datetime = datetime.strptime(birthdate, '%d/%m/%Y')
    age = current_year - birthdate_datetime.year
    return age





