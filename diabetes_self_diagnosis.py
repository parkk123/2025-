import json

class DiseaseDiagnosis:
    def __init__(self, name, age, blood_type, gender, symptoms, lifestyle):
        self.name = name
        self.age = age
        self.blood_type = blood_type
        self.gender = gender
        self.symptoms = symptoms
        self.lifestyle = lifestyle  # 생활 습관 추가

    def diagnose(self):
        """당뇨병 자가진단을 위한 메소드"""
        possible_diseases = []

        # 당뇨병과 관련된 증상 체크
        if "피로감" in self.symptoms and "체중 감소" in self.symptoms:
            possible_diseases.append("당뇨병 가능성 있습니다.")
        
        if "다음증" in self.symptoms and "시야 흐림" in self.symptoms:
            possible_diseases.append("당뇨병 가능성 있습니다.")
        
        # 생활 습관에 따른 추가적인 리스크 체크
        if self.lifestyle["운동 부족"] == "예" or self.lifestyle["과도한 음주"] == "예":
            possible_diseases.append("당뇨병 위험 요인 있음. 운동과 음주 개선이 필요합니다.")

        # 당뇨병에 대한 조기 경고
        if self.age > 45 and "비만" in self.symptoms:
            possible_diseases.append("당뇨병을 예방하려면 생활습관 개선이 필요합니다.")

        if not possible_diseases:
            possible_diseases.append("당뇨병 관련 증상 및 위험이 없습니다. 건강한 생활을 유지하세요.")

        return possible_diseases

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

def load_from_json():
    try:
        with open("diabetes_diagnosis.json", "r") as file:
            data = json.load(file)
            diagnosis = DiseaseDiagnosis(data["name"], data["age"], data["blood_type"], data["gender"], data["symptoms"], data["lifestyle"])
            return diagnosis
    except FileNotFoundError:
        return None

def get_user_input():
    name = input("이름을 입력하세요: ")
    age = int(input("나이를 입력하세요: "))
    blood_type = input("혈액형을 입력하세요 (예: A, B, AB, O): ")
    gender = input("성별을 입력하세요 (남/여): ")

    symptoms = input("증상을 쉼표로 구분하여 입력하세요 (예: 피로감, 체중 감소, 다뇨증): ").split(",")
    symptoms = [symptom.strip() for symptom in symptoms]  # 공백 제거

    # 생활 습관 관련 질문
    lifestyle = {
        "운동 부족": input("운동을 자주 하지 않으시나요? (예/아니오): "),
        "과도한 음주": input("과도한 음주 습관이 있나요? (예/아니오): "),
        "비만": input("체중이 과체중인가요? (예/아니오): ")
    }

    return DiseaseDiagnosis(name, age, blood_type, gender, symptoms, lifestyle)

def main():
    print("생활 습관 기반 당뇨병 자가 진단 프로그램")

    diagnosis = get_user_input()

    print(f"\n{diagnosis.name}님의 진단 결과:")
    for disease in diagnosis.diagnose():
        print(disease)

    save_to_json(diagnosis)

    print("\n저장된 진단 결과:")
    saved_diagnosis = load_from_json()
    if saved_diagnosis:
        print(f"이름: {saved_diagnosis.name}, 나이: {saved_diagnosis.age}, 혈액형: {saved_diagnosis.blood_type}, 성별: {saved_diagnosis.gender}")
        print(f"증상: {', '.join(saved_diagnosis.symptoms)}")
        print("진단 결과:")
        for disease in saved_diagnosis.diagnose():
            print(disease)

if __name__ == "__main__":
    main()