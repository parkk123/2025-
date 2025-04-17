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

    from diagnosis import DiseaseDiagnosis
    return DiseaseDiagnosis(name, age, blood_type, gender, symptoms, lifestyle)
