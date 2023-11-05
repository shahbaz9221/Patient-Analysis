from file_handling import read_patient_data
from patient_data_processing import merge_patient_data_with_build, find_worst_patients, sort_patients_by_condition, generate_priority_referral_decisions
from bmi_calculation import calculate_bmi_for_athletic_build, calculate_bmi_for_regular_build, calculate_bmi_for_slim_build

def display_data(data):
    """
    Display a list of data elements.

    Args:
    data (list): A list of data elements to display.

    Returns:
    None: The function prints the data elements.
    """
    for value in data:
        print(value)

def main(file_path):
    """
    Main function to process patient data and generate priority-based referral decisions.

    Args:
    file_path (str): The path to the patient data file.

    Returns:
    None: The function processes and displays patient data and referral decisions.
    """
    reader = read_patient_data(file_path)

    BMI_for_slim = calculate_bmi_for_slim_build(reader)
    display_data(BMI_for_slim)

    BMI_for_regular = calculate_bmi_for_regular_build(reader)
    display_data(BMI_for_regular)

    BMI_for_athletic = calculate_bmi_for_athletic_build(reader)
    display_data(BMI_for_athletic)

    build_patient_data = merge_patient_data_with_build(reader, BMI_for_regular)
    display_data(build_patient_data)

    find_worst_patients(build_patient_data)

    sorted_patients = sort_patients_by_condition(build_patient_data)
    display_data(sorted_patients)

    generate_priority_referral_decisions(build_patient_data)

if __name__ == '__main':
    main("DADSA 2021 CWK B DATA COLLECTION.csv")
