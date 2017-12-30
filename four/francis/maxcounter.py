def solution(N, A):
    max_value = 0
    tmp_max_value = 0
    counters = {}
    for i in A:
        if 1 <= i <= N:
            if i in counters:
                counters[i] += 1
            else:
                counters[i] = 1
            tmp_max_value = max(tmp_max_value, counters[i])
        else:
            max_value += tmp_max_value
            tmp_max_value = 0
            counters = {}
    return [max_value + (counters[x] if x in counters else 0) for x in range(1, N+1)]
