def get_card_cnt(cards):
    card_cnt = [0] * 10
    for x in cards:
        card_cnt[x] += 1
    return card_cnt


num_list = []


def card_pick(level, max_level, card_cnt, card_used, number):
    if level == max_level:
        num_list.append(number)
        return

    for i in range(1, 10):
        if card_cnt[i] > card_used[i]:
            card_used[i] += 1
            card_pick(level + 1, max_level, card_cnt, card_used, number * 10 + i)
            card_used[i] -= 1


def solution(card, n):
    # 여기에 코드를 작성해주세요.
    card_cnt = get_card_cnt(card)
    x = list(map(int, str(n)))
    x_cnt = get_card_cnt(x)
    if card_cnt == x_cnt:
        num_list.clear()
        card_pick(0, len(card), card_cnt, [0] * 10, 0)
        ans = num_list.index(n) + 1
    else:
        ans = -1
    return ans


# 아래는 테스트케이스 출력을 해보기 위한 코드입니다.
card1 = [1, 2, 1, 3]
n1 = 1312
ret1 = solution(card1, n1)
for i in range(len(num_list)):
    print(num_list[i])
# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은 ", ret1, " 입니다.")

# 아래는 테스트케이스 출력을 해보기 위한 코드입니다.
card2 = [1, 1, 1, 2]
n2 = 1122
ret2 = solution(card2, n2)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은 ", ret2, " 입니다.")
