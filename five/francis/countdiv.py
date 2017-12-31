def solution(A, B, K):
    return int(B/K) - int(A/K) + (1 if A % K == 0 else 1)