# Func này gấp đôi arr lên
def func_a(arr):
    ret = arr + arr
    return ret

# 
def func_b(first, second):
    MAX_NUMBER = 1001
    # Tạo 1 mảng 1001 số 0
    counter = [0 for _ in range(MAX_NUMBER)]
    # Kiểm tra xem trái có giống phải hay không
    # Nếu như mảng đầu có phần từ thì tăng 1, mảng 2 có phần tử giống vậy thì giảm đi
    for f, s in zip(first, second):
        counter[f] += 1
        counter[s] -= 1
    # Kết quả là nếu như có các phần tử giống nhau thì tất cả là 0
    for c in counter:
        if c != 0:
            return False
    return True

# Kiểm tra các đảo ngược xem có cái nào bằng second không
def func_c(first, second):
    length = len(second)
    for i in range(length):
        if first[i : i + length] == second:
            return True
    return False

def solution(arrA, arrB):
    if len(arrA) != len(arrB):
        return False
    if func_b(arrA, arrB):
        arrA_temp = func_a(arrA)
        if func_c(arrA_temp, arrB):
            return True
    return False

#아래는 테스트케이스 출력을 해보기 위한 코드입니다. 
arrA1 = [1, 2, 3, 4]
arrB1 = [3, 4, 1, 2]
ret1 = solution(arrA1, arrB1)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret1, "입니다.")

arrA2 = [1, 2, 3, 4]
arrB2 = [1, 4, 2, 3]
ret2 = solution(arrA2, arrB2)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret2, "입니다.")