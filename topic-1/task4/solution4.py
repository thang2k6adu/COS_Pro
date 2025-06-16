def solution(num):
    num += 1
    result = ''.join('1' if x == '0' else x for x in str(num))
    return result

num = 999999999999999999
ret = solution(num)
print(ret)  # Output: 10000000