# Ý tưởng:
# Lưu giá mua thấp nhất
# Lưu giá bán cao nhất
# Tính hiệu số giữa giá bán và giá mua

def solution(prices):
    INF = 1000000001
    temp = INF
    answer = -INF
    for price in prices:
        # Tìm ngày nên bán (có hiệu giá cao nhất)
        if tmp != INF:
            answer = max(answer, price - tmp)
        # Tìm ngày nên mua (có giá thấp nhất)
        # Cập nhật để ngày sau dùng
        # Nếu tìm giá trước thì (bán luôn trong ngày trong trường hợp giá = 0 là lợi nhuận cao nhất), vi phạm quy tắc
        tmp = min(tmp, price)
    return answer