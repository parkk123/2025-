from user_input import get_user_input
from file_manager import save_to_json, load_from_json

def main():
    print("생활 습관 기반 당뇨병 자가 진단 프로그램")

    # 사용자로부터 기본 정보와 증상 입력받기
    diagnosis = get_user_input()

    # 진단 결과 출력
    print(f"\n{diagnosis.name}님의 진단 결과:")
    for disease in diagnosis.diagnose():
        print(disease)

    # 결과를 JSON 파일로 저장
    save_to_json(diagnosis)

    # 저장된 데이터를 JSON 파일에서 불러오기
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