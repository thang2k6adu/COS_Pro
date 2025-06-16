def func_a(string, length):
    padSize = length - len(string)
    return "0"*padSize + string if padSize > 0 else string

def solution(binaryA, binaryB):
    max_length = max(len(binaryA), len(binaryB))
    binaryA = func_a(binaryA, max_length)
    binaryB = func_a(binaryB, max_length)

    hamming_distance = 0
    for a, b in zip(binaryA, binaryB):
        if a != b:
            hamming_distance += 1
    return hamming_distance

binaryA = '10010'
binaryB = '110'

print(solution(binaryA, binaryB))  # Output: 2