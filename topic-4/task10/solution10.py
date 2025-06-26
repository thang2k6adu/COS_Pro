import math

def get_primes(b):
    e = int(math.sqrt(b)) + 1 #ở đây chỉ lấy tới căn b, nếu lớn hơn thì bình phương lên > b, phí
    is_prime = [0] * e

    primes = []

    for i in range(2, e):
        if is_prime[i] == 0:
            primes.append(i)
        for j in range(i + i, e, i):
            is_prime[j] = 1
    print(primes)
    return primes

def solution(a, b):
    prime = get_primes(b)
    answer = 0
    print(prime)
    for p in prime:
        t1, t2 = p**2, p**3
        print(t1, ' ', t2)
        if a <= t1 <= b: answer += 1
        if a <= t2 <= b: answer +=1
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
a =  6
b =  30
ret = solution(a, b)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")