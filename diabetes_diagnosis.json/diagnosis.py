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