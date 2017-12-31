def solution(S, P, Q):
    impact_map = {
        'A': 1,
        'C': 2,
        'G': 3,
        'T': 4,
    }
    counts = {x: 0 for x in impact_map.keys()}
    tmp = counts.copy()
    prefix_sum = [tmp]
    for i in S:
        counts[i] += 1
        tmp = counts.copy()
        prefix_sum.append(tmp)
    answers = []
    for i in range(len(P)):
        diff = {}
        for k in impact_map.keys():
            diff[k] = prefix_sum[Q[i]+1][k] - prefix_sum[P[i]][k]
        min_impact = float('inf')
        for k, v in diff.items():
            if v != 0:
                min_impact = min(min_impact, impact_map[k])
            if min_impact == 1:
                break
        answers.append(min_impact)
    return answers
