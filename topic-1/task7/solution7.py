def solution(arrA, arrB):
    arrA_idx = 0
    arrB_idx = 0
    result = []

    while arrA_idx < len(arrA) and arrB_idx < len(arrB):
        if arrA[arrA_idx] < arrB[arrB_idx]:
            result.append(arrA[arrA_idx])
            arrA_idx += 1
        else:
            result.append(arrB[arrB_idx])
            arrB_idx += 1
    while arrA_idx < len(arrA):
        result.append(arrA[arrA_idx])
        arrA_idx += 1
    while arrB_idx < len(arrB):
        result.append(arrB[arrB_idx])
        arrB_idx += 1

    return result

arrA = [-2, 3, 5, 9]
arrB = [0, 1, 5]
ret = solution(arrA, arrB)

#Press Run button to receive output.
print("Solution: return value of the function is ", ret, " .")