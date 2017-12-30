def solution(A):
    possible_mins = {1: 1}
    for i in A:
        if i > 0:
            possible_mins[i+1] = 1
    for i in A:
        if i in possible_mins:
            del possible_mins[i]
    min_value = float('inf')
    for i in possible_mins.keys():
        min_value = min(min_value, i)
    return min_value