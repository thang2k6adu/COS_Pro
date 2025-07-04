# Kiểm tra xem s có ở trong mảng arr hay không
def func_a(arr, s):
    return s in arr

# Kiểm tra xem có phải là palidrome hay không
def func_b(s):
    length = len(s)
    for i in range(length // 2):
        if s[i] != s[length - i - 1]:
            return False
    return True

# Lấy ra palidrome thứ k
def func_c(palindromes, k):
    palindromes = sorted(palindromes)
    if len(palindromes) < k:
        return "NULL"
    else:
        return palindromes[k - 1]

def solution(s, k):
    palindromes = []
    length = len(s)
    for start_idx in range(length):
        for cnt in range(1, length - start_idx + 1):
            sub_s = s[start_idx : start_idx + cnt]
            if func_b(sub_s) == True:
                if func_a(palindromes, sub_s) == False:
                    palindromes.append(sub_s)

    answer = func_c(palindromes, k)
    return answer


#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
s1 = "abcba"
k1 = 4
ret1 = solution(s1, k1)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret1, "입니다.")

s2 = "ccddcc"
k2 = 7
ret2 = solution(s2, k2)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret2, "입니다.")