def solution(n):
    a = [[0] * n for _ in range(n)]
    # Biến xác định hướng đi (0 : phải, 1: xuống, 2: trái, 3: lên)
    dir = 0
    # Loop sẽ giảm 1 mỗi khi đi xuống hoặc đi lên
    loop = n
    # Tọa độ ban đầu (nếu như sang phải thì sẽ lên (0,0))
    r, c = 0, -1
    # Nếu sang phải thì sẽ là cộng (0, 1), xuống dưới thì là cộng (1, 0)
    # Sang trái thì cộng (0, -1), lên trên thì cộng (-1, 0)
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    num = 0

    while num < n * n:
        for _ in range(loop):
            r += dr[dir]
            c += dc[dir]
            num += 1
            a[r][c] = num

        # Chuyển sang hướng tiếp theo
        dir = (dir + 1) % 4
        # Nếu đi xuống hoặc đi lên thì giảm loop (đi xuống là 1 nhưng)
        if dir % 2 == 1:
            loop -= 1
    result = 0
    for x in range(n):
        result += a[x][x]
    return result

n1 = 3
ret = solution(n1)
print(ret)  # Output: 15