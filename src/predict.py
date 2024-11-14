def get_user_input():
    try:
        pregnancies = int(input("Enter number of pregnancies: "))
        glucose = int(input("Enter glucose level: "))
        blood_pressure = int(input("Enter blood pressure level: "))
        skin_thickness = int(input("Enter skin thickness: "))
        insulin = int(input("Enter insulin level: "))
        bmi = float(input("Enter BMI: "))
        diabetes_pedigree = float(input("Enter diabetes pedigree function: "))
        age = int(input("Enter age: "))
        return [[pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree, age]]
    except ValueError:
        print("Invalid input. Please enter valid numerical values.")
        return get_user_input()

def predict_diabetes(model, input_data):
    prediction = model.predict(input_data)
    if prediction[0] == 1:
        print("Diabetic")
    else:
        print("Not Diabetic")
