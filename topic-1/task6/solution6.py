def solution(pos):
    r = ord(pos[0]) - ord('A')
    c = ord(pos[1]) - ord('1')

    dr = [2, 1, -1, -2, -2, -1, 1, 2]
    dc = [1, 2, 2, 1, -1, -2, -2, -1]

    answer = 0
    for i in range(8):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < 8 and 0 <= nc < 8:
            answer += 1
    return answer

pos = 'A7'
ret = solution(pos)

print(ret)