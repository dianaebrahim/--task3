patients = [
    {"name": "Ahmed", "blood_sugar": 180},
    {"name": "Sara", "blood_sugar": 90},
    {"name": "Omar", "blood_sugar": 220},
    {"name": "Layla", "blood_sugar": 110},
    {"name": "Khaled", "blood_sugar": 150},
    {"name": "Youssef", "blood_sugar": 250},
    {"name": "Fatima", "blood_sugar": 85},
    {"name": "Mahmoud", "blood_sugar": 195},
    {"name": "Amina", "blood_sugar": 140},
    {"name": "Hassan", "blood_sugar": 175}
]

def categorize(patient):
    if patient["blood_sugar"] < 70 or patient["blood_sugar"] > 200:
        return 0  # حالة حرجة
    elif 70 <= patient["blood_sugar"] <= 120:
        return 1  # حالة طبيعية
    else:
        return 2  # حالة متوسطة

sorted_patients = sorted(patients, key=categorize)

print("المرضى حسب الأولوية الطبية:")
for patient in sorted_patients:
    print(f"{patient['name']}: {patient['blood_sugar']} mg/dL")