def solution(A):
    length = len(A)
    checks = [0] * (length+1)
    for i in A:
        if i > length:
            return 0
        if checks[i-1] == 1:
            return 0
        else:
            checks[i-1] = 1
    return 1
