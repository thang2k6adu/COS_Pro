def func_a(numA, numB, exp):
    if exp == "+":
        return numA + numB
    elif exp == "-":
        return numA - numB
    elif exp == "*":
        return numA * numB


def func_b(exp):
    for index, value in enumerate(exp):
        if value == "+" or value == "-" or value == "*":
            return index


def func_c(exp, idx):
    numA = int(exp[:idx])
    numB = int(exp[idx + 1 :])
    return numA, numB


def solution(exp):
    exp_idx = func_b(exp)
    numA, numB = func_c(exp, exp_idx)
    result = func_a(numA, numB, exp[exp_idx])
    return result


expression = "123+12"
ret = solution(expression)

print(ret)  # Output: 135