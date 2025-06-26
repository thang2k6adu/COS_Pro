# 다음과 같이 import를 사용할 수 있습니다.
# import math


def solution(hour, minute):
    hour_deg = (hour / 12) * 360
    minute_deg = minute / 60
    deg = abs(hour_deg - minute_deg)
    deg = deg if deg <= 180 else 360 - deg

    answer = '{:.1f}'.format(deg)
    return answer


# 아래는 테스트케이스 출력을 해보기 위한 코드입니다.
hour = 7
minute = 0
ret = solution(hour, minute)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은 ", ret, " 입니다.")
