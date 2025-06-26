#다음과 같이 import를 사용할 수 있습니다.
#import math

def solution(bishops):
    # Khởi tạo bàn cờ
    a = [[0]*9 for _ in range(9)]
    dxy = [ [1, 1], [1, -1], [-1, -1], [-1, 1]]

    for bishop in bishops:
        x = ord(bishop[0]) - ord('A') + 1
        y = int(bishop[1])

        a[y][x] = 1
        for dx, dy in dxy:
            nx = x
            ny = y
            while True:
                nx += dx
                ny += dy
                if nx > 8 or nx < 1 or ny > 8 or ny < 1: break
                a[ny][nx] = 1
    
    answer = 0
    for y in range(1, 9):
        for x in range(1, 9):
            if not a[y][x]:
                answer += 1
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
bishops1 = ["D5"]
ret1 = solution(bishops1)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret1, "입니다.")

bishops2 = ["D5", "E8", "G2"]
ret2 = solution(bishops2)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret2, "입니다.")

# Ý tưởng
# Tạo ra mảng đường đi
# Xác định vị trí hiện tại và đánh dấu
# Với mỗi bishop, xét cả 4 hướng đi đên khi nào x và y > 8 và nhỏ hơn 1 thì dứng