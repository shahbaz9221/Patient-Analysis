import csv
def read_file():
    with open('DADSA 2021 CWK B DATA COLLECTION.csv', 'r') as csv_file:
        read_from_file = csv.reader(csv_file)
        array=[]
        next(read_from_file)
        for  reader in read_from_file: 
            array.append({'Name':reader[0], 'Date_of_birth':reader[1], 'Sex':reader[2],'Height':reader[3], 'Weight':reader[4], 'Smoker':reader[5] or 'N', 'Asthmatic':reader[6] or 'N', 'NJT/NGR':reader[7] or 'N', 'Hypertension':reader[8] or 'N', 'Renal RT':reader[9] or 'N', 'Ileostomy':reader[10] or 'N','Parenteral Nutrition':reader[11]})
        #display(array)
        return array


def Display(temp):
    for value in temp:
        print(value)


def Calculte_BMI_for_Slim(temp):
    new_list =[]
    for value in temp:
        height=float(value['Height']) ** 2
        weight=float(value['Weight'])
        bmi = float(weight/height)
        if bmi < 18.5:
            new_list.append({'Build':'Slim' , 'BMI':bmi, 'Condition':'Underweight'})
        elif bmi >=18.5 and bmi <25:
            new_list.append({'Build':'Slim' , 'BMI':bmi, 'Condition':'Normal'})
        elif bmi >= 25 and bmi <28:
            new_list.append({'Build':'Slim' , 'BMI':bmi, 'Condition':'Overweight'})
        else:
            new_list.append({'Build':'Slim' , 'BMI':bmi, 'Condition':'Obese'})
    return new_list


def Calculte_BMI_for_regular(temp):
    new_list =[]
    for value in temp:
        height=float(value['Height']) ** 2
        weight=float(value['Weight'])
        bmi = float(weight/height)
        if bmi < 18.5:
            new_list.append({'Build':'Regular' , 'BMI':bmi, 'Condition':'Underweight'})
        elif bmi >=18.5 and bmi <25:
            new_list.append({'Build':'Regular' , 'BMI':bmi, 'Condition':'Normal'})
        elif bmi >= 25 and bmi <29:
            new_list.append({'Build':'Regular' , 'BMI':bmi, 'Condition':'Overweight'})
        else:
            new_list.append({'Build':'Regular' , 'BMI':bmi, 'Condition':'Obese'})
    return new_list


def Calculte_BMI_for_Athletic(temp):
    new_list =[]
    for value in temp:
        height=float(value['Height']) ** 2
        weight=float(value['Weight'])
        bmi = float(weight/height)
        if bmi < 18.5:
            new_list.append({'Build':'Athletic' , 'BMI':bmi, 'Condition':'Underweight'})
        elif bmi >=18.5 and bmi <25:
            new_list.append({'Build':'Athletic' , 'BMI':bmi, 'Condition':'Normal'})
        elif bmi >= 25 and bmi <30:
            new_list.append({'Build':'Athletic' , 'BMI':bmi, 'Condition':'Overweight'})
        else:
            new_list.append({'Build':'Athletic' , 'BMI':bmi, 'Condition':'Obese'})
    return new_list

def updated_array(patients,build):
    index=0
    updated_list=[]
    for value in patients:
        updated_list.append({'patients_list':value,'build_table':build[index]})
        index = index + 1
    return updated_list


def calculate_age(date):
    date_split=date.split('/')
    current_year = 2021
    age = current_year - int(date_split[2])
    return age


def calculating_priorty(priorty_list):
    for val in priorty_list:
        if val['Priorty'] == "1":
            print(val['Name'], val['Condition'], val['Decision'])
    for val in priorty_list:
        if val['Priorty'] == "2":
            print(val['Name'], val['Condition'], val['Decision'])
    for val in priorty_list:
        if val['Priorty'] == "3":
            print(val['Name'], val['Condition'], val['Decision'])   
    for val in priorty_list:
        if val['Priorty'] == "4":
            print(val['Name'], val['Condition'], val['Decision'])
    for val in priorty_list:
        if val['Priorty'] == "5":
            print(val['Name'], val['Condition'], val['Decision'])
    for val in priorty_list:
        if val['Priorty'] == "6":
            print(val['Name'], val['Condition'], val['Decision'])
    for val in priorty_list:
        if val['Priorty'] == "7":
            print(val['Name'], val['Condition'], val['Decision'])

    
def sorting_on_condition(patients_list):
    sorted_patients = []
    
    for value in range(len(patients_list)):
        if patients_list[value]['build_table']['Condition'] == "Obese":
            sorted_patients.append({'Name':patients_list[value]['patients_list']['Name'], 'Age':calculate_age(patients_list[value]['patients_list']['Date_of_birth']), 'BMI':patients_list[value]['build_table']['BMI'],'Condition':patients_list[value]['build_table']['Condition']})
    
    for value in range(len(patients_list)):
        if patients_list[value]['build_table']['Condition'] == "Underweight":
            sorted_patients.append({'Name':patients_list[value]['patients_list']['Name'], 'Age':calculate_age(patients_list[value]['patients_list']['Date_of_birth']), 'BMI':patients_list[value]['build_table']['BMI'],'Condition':patients_list[value]['build_table']['Condition']})
    
    for value in range(len(patients_list)):
        if patients_list[value]['build_table']['Condition'] == "Overweight":
            sorted_patients.append({'Name':patients_list[value]['patients_list']['Name'], 'Age':calculate_age(patients_list[value]['patients_list']['Date_of_birth']), 'BMI':patients_list[value]['build_table']['BMI'],'Condition':patients_list[value]['build_table']['Condition']})

    for value in range(len(patients_list)):
        if patients_list[value]['build_table']['Condition'] == "Normal":
            sorted_patients.append({'Name':patients_list[value]['patients_list']['Name'], 'Age':calculate_age(patients_list[value]['patients_list']['Date_of_birth']), 'BMI':patients_list[value]['build_table']['BMI'],'Condition':patients_list[value]['build_table']['Condition']})
    Display(sorted_patients)


def worst_patients(worst_patients):
        patient_count = 0
        for value in range(len(worst_patients)):
            if worst_patients[value]['build_table']['Condition'] == "Obese" or worst_patients[value]['build_table']['Condition'] == "Overweight":
                if worst_patients[value]['patients_list']['Sex'] == "M" and calculate_age(worst_patients[value]['patients_list']['Date_of_birth'])> 15:
                    patient_count = patient_count + 1
                    print(worst_patients[value]['patients_list']['Name'], calculate_age(worst_patients[value]['patients_list']['Date_of_birth']),worst_patients[value]['build_table']['Condition'])
            elif worst_patients[value]['build_table']['Condition'] == "Obese" or worst_patients[value]['build_table']['Condition'] == "Overweight":
                if worst_patients[value]['patients_list']['sex'] == "F" and calculate_age(worst_patients[value]['patients_list']['Date_of_birth'])> 15:
                    patient_count = patient_count + 1
                    print(worst_patients[value]['patients_list']['Name'], calculate_age(worst_patients[value]['patients_list']['Date_of_birth']),worst_patients[value]['build_table']['Condition'])
            if patient_count == 10:
                break


def refer_table(patients):
        decision_arr=[]
        for value in range(len(patients)):
            if (patients[value]['build_table']['Condition'] == "Obese" or patients[value]['build_table']['Condition'] == "Underweight") and calculate_age(patients[value]['patients_list']['Date_of_birth']) > 55:
                decision_arr.append({'Priorty': '1','Condition': 'Obese OR Underweight', 'Name':patients[value]['patients_list']['Name'], 'Decision': 'refer'})
            
            elif patients[value]['patients_list']['Hypertension'] == "Y":
                decision_arr.append({'Priorty': '2','Condition': 'Hypertension', 'Name':patients[value]['patients_list']['Name'], 'Decision': 'refer'})
            
            elif patients[value]['patients_list']['Asthmatic'] == "Y" or patients[value]['patients_list']['Smoker'] == "Y":
                decision_arr.append({'Priorty': '3','Condition': 'Asthamatic Or Smoker', 'Name':patients[value]['patients_list']['Name'], 'Decision': 'refer'})
            
            elif patients[value]['patients_list']['NJT/NGR'] == "Y":
                decision_arr.append({'Priorty': '4','Condition': 'NJT Or NGR', 'Name':patients[value]['patients_list']['Name'], 'Decision': 'refer'})
            
            elif patients[value]['patients_list']['Renal RT'] == "Y":
                decision_arr.append({'Priorty': '5','Condition': 'Renal Replacement Therapy', 'Name':patients[value]['patients_list']['Name'], 'Decision': 'refer'})
            
            elif patients[value]['patients_list']['Ileostomy'] == "Y":
                decision_arr.append({'Priorty': '6','Condition': 'Ileostomy', 'Name':patients[value]['patients_list']['Name'], 'Decision': 'refer'})
            
            else:
                decision_arr.append({'Priorty': '7','Condition': 'Parental Nutrition', 'Name':patients[value]['patients_list']['Name'], 'Decision': 'refer'})
        calculating_priorty(decision_arr)
        
reader = []
reader = read_file()

BMI_for_slim=[]
BMI_for_slim=Calculte_BMI_for_Slim(reader)
#display(BMI_for_regular)

BMI_for_regular=[]
BMI_for_regular=Calculte_BMI_for_regular(reader)
#display(BMI_for_regular)

BMI_for_athletic=[]
BMI_for_athletic=Calculte_BMI_for_Athletic(reader)
#display(BMI_for_athletic)

patients_updated_array=[]
patients_updated_array=updated_array(reader,BMI_for_regular)
#Display(my_updated_array)

worst_patients(patients_updated_array)
sorting_on_condition(patients_updated_array)

refer_table(patients_updated_array)

