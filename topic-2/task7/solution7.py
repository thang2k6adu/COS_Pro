def solution(money):
    coin = [10, 50, 100, 500, 1000, 5000, 10000, 50000]
    counter = 0
    idx = len(coin) - 1
    while money:
        counter += money // coin[idx]
        money %= coin[idx]
        idx -= 1
    return counter

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
money = 2760
ret = solution(money)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")
# Ý tưởng
# chia số tiền hiện tại lần lượt cho tiền từ to tới bé (chia lấy phần nguyên)
# Số tiền còn lại sẽ là chia lấy dư
# Ví dụ muốn xem 20 chia được thành bao nhiêu 5
# Nếu dơn giản thì là 20 - 5 rồi đếm, hoặc là chia lấy nguyên 20 // 5
# Số tiền thừa sẽ là 20 % 5 = 0 (dĩ nhiên, nếu 23 thì dư 3k)