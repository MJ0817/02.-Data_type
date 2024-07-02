def calculate_risk_score(exposure_level, height_work, electrical_equipment):
    """위험 점수를 계산하는 함수"""
    # 위험 요소들의 가중치와 점수 설정 (임의의 값)
    weights = [0.5, 0.3, 0.2]  # 각 요소의 가중치
    scores = [exposure_level, height_work, electrical_equipment]  # 각 요소의 점수 (1~10 점 사이)

    # 가중 평균을 이용한 전체 위험 점수 계산
    total_score = sum(w * s for w, s in zip(weights, scores))

    return total_score


def main():
    print("=== 위험 평가 계산기 ===")

    print("화학물질 노출 수준 (1~10 사이의 점수 입력):")
    exposure_level = float(input())

    print("높은 고도 작업 위험 수준 (1~10 사이의 점수 입력):")
    height_work = float(input())

    print("전기 장비 사용 위험 수준 (1~10 사이의 점수 입력):")
    electrical_equipment = float(input())

    # 전체 위험 점수 계산
    total_risk_score = calculate_risk_score(exposure_level, height_work, electrical_equipment)

    print(f"\n전체 위험 점수: {total_risk_score:.2f}")

    # 위험 수준에 따른 안전성 평가
    if total_risk_score < 3:
        print("안전")
    elif total_risk_score < 7:
        print("보통")
    else:
        print("위험")


if __name__ == "__main__":
    main()
