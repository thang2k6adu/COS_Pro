def winnerA(record):
    if record == 0:
        return 1
    elif record == 1:
        return 2
    return 0

def solution(recordA, recordB):
    posA = 0

    for i in range(10):
        if recordA[i] == recordB[i]:
            continue
        elif recordA[i] == winnerA(recordB[i]):
            posA +=3
        else:
            posA = max(0, posA - 1)
        
    return posA

recordA = [2,0,0,0,0,0,1,1,0,0]
recordB = [0,0,0,0,2,2,0,2,2,2]
ret = solution(recordA, recordB)


#Press Run button to receive output.
print("Solution: return value of the function is", ret, ".")