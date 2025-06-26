# 다음과 같이 import를 사용할 수 있습니다.
# import math


def solution(commands):
    # 여기에 코드를 작성해주세요.
    # answer = [0, 0]
    # command_list = [char for char in commands]

    # for command in command_list:
    #     if command == "U":
    #         answer[1] += 1
    #     elif command == "D":
    #         answer[1] -= 1
    #     elif command == "L":
    #         answer[0] -= 1
    #     else:
    #         answer[0] += 1
    move = dict(zip("LRUD", [[-1, 0], [1, 0], [0, 1], [0, -1]]))
    answer = [0, 0]

    for command in commands:
        m = move[command]
        answer[0] += m[0]
        answer[1] += m[1]
    return answer


# 아래는 테스트케이스 출력을 해보기 위한 코드입니다.
commands = "URDDL"
ret = solution(commands)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은 ", ret, " 입니다.")
