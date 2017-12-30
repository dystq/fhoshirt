def solution(X, A):
    leaves = {x:1 for x in range(1, X+1)}
    for i in range(len(A)):
        if A[i] in leaves:
            del leaves[A[i]]
        if len(leaves) == 0:
            return i
    return -1
