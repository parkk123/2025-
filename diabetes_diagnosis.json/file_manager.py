import json

# 진단 결과를 JSON 파일로 저장하는 함수
def save_to_json(diagnosis):
    disease_data = {
        "name": diagnosis.name,
        "age": diagnosis.age,
        "blood_type": diagnosis.blood_type,
        "gender": diagnosis.gender,
        "symptoms": diagnosis.symptoms,
        "lifestyle": diagnosis.lifestyle,
        "diagnosis": diagnosis.diagnose()
    }
    with open("diabetes_diagnosis.json", "w") as file:
        json.dump(disease_data, file, indent=4)

# JSON 파일에서 사용자의 진단 데이터를 불러오는 함수
def load_from_json():
    try:
        with open("diabetes_diagnosis.json", "r") as file:
            data = json.load(file)
            from diagnosis import DiseaseDiagnosis
            diagnosis = DiseaseDiagnosis(data["name"], data["age"], data["blood_type"], data["gender"], data["symptoms"], data["lifestyle"])
            return diagnosis
    except FileNotFoundError:
        return None