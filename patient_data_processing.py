from constants import PATIENT_NAME, DATE_OF_BIRTH
from patient_utils import calculate_age_from_birthdate

def merge_patient_data_with_build(patients, build):
    """
    Merge patient data with corresponding build information.

    Combines a list of patient data with a list of corresponding build information.
    Each patient entry is paired with its corresponding build, resulting in a list of dictionaries.

    Args:
    patients (list): A list of patient data.
    build (list): A list of build information corresponding to each patient.

    Returns:
    list: A list of dictionaries, each containing patient data and build information.
    """
    return [{'patient_data': patient, 'build_info': b} for patient, b in zip(patients, build)]


def find_worst_patients(patients, current_year=2021, age_threshold=15):
    """
    Find and print information about worst patients based on build condition.

    Filters and prints information about patients who are 'Obese' or 'Overweight'
    based on their build condition and age.

    Args:
    patients (list): A list of patient data and build information.
    current_year (int, optional): The current year. Default is 2021.
    age_threshold (int, optional): The age threshold to consider patients. Default is 15.

    Returns:
    None: The function prints patient information and does not return a value.
    """
    for patient in patients:
        build_condition = patient['build_info']['Condition']
        patient_data = patient['patient_data']
        
        if build_condition in ("Obese", "Overweight") and calculate_age_from_birthdate(patient_data[DATE_OF_BIRTH], current_year) > age_threshold:
            print(patient_data[PATIENT_NAME], calculate_age_from_birthdate(patient_data[DATE_OF_BIRTH], current_year), build_condition)



def sort_patients_by_condition(patient_data, current_year=2021):
    """
    Sort patients based on their build condition and extract relevant information.

    Sorts and extracts patient information based on their build condition and calculates
    their age. The patients are sorted in the order of "Obese," "Underweight," "Overweight," and then "Normal."

    Args:
    patient_data (list): A list of patient data and build information.
    current_year (int, optional): The current year. Default is 2021.

    Returns:
    list: A list of dictionaries containing sorted patient information, including
        'Patient Name', 'Age', 'BMI', and 'Condition'.
    """
    sorted_patients = []

    # Sort patients by custom order: Obese, Underweight, Overweight, Normal
    custom_sort_order = {"Obese": 1, "Underweight": 2, "Overweight": 3, "Normal": 4}

    for patient in patient_data:
        patient_info = {
            'Patient Name': patient['patient_data'][PATIENT_NAME],
            'Age': calculate_age_from_birthdate(patient['patient_data'][DATE_OF_BIRTH], current_year),
            'BMI': patient['build_info']['BMI'],
            'Condition': patient['build_info']['Condition']
        }
        sorted_patients.append(patient_info)

    sorted_patients.sort(key=lambda x: custom_sort_order[x['Condition']])

    return sorted_patients

def generate_priority_referral_decisions(patients, current_year=2021):
    """
    Generate and print priority-based referral decisions for patients based on their medical conditions.

    This function analyzes patient data and assigns referral decisions based on specific medical conditions.
    Referral decisions are printed according to their assigned priority.

    Args:
    patients (list of dict): A list of patient data and medical condition information.
    current_year (int, optional): The current year. Default is 2021.

    Returns:
    None: The function prints referral decisions.
    """
    priority_dict = {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: []}

    for patient in patients:
        patient_data = patient['patient_data']
        condition = patient.get('build_info').get('Condition')

        if condition in ("Obese", "Underweight") and calculate_age_from_birthdate(patient_data[DATE_OF_BIRTH], current_year) > 55:
            priority = 1
        elif patient_data['Hypertension'] == "Y":
            priority = 2
        elif patient_data['Asthmatic'] == "Y" or patient_data['Smoker'] == "Y":
            priority = 3
        elif patient_data['NJT / NGR'] == "Y":
            priority = 4
        elif patient_data['Renal RT'] == "Y":
            priority = 5
        elif patient_data['Ileostomy / Colostomy'] == "Y":
            priority = 6
        else:
            priority = 7

        priority_dict[priority].append({
            'Condition': condition,
            'Patient Name': patient_data[PATIENT_NAME],
            'Decision': 'refer'
        })

    # Print referral decisions by priority
    for priority, priority_value in priority_dict.items():
        for patient in priority_value:
            print(patient[PATIENT_NAME], patient['Condition'], patient['Decision'])