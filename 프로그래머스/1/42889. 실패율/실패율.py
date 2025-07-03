def solution(N, stages):
    answer = []
    for i in range(1, N+1):
        answer.append([i, 0])
    
    stages.sort(reverse =True)
    cnt = 0
    i = 0

    while i < len(stages):
        cur_stage = stages[i]
        cnt = stages.count(cur_stage)

        if cur_stage == N+1:
            i += stages.count(cur_stage)
            continue

        i += stages.count(cur_stage)
        answer[cur_stage-1][1] = cnt/i

    answer.sort(key = lambda n: (-n[1], n[0]))
    
    l = [s for s, _ in answer]
    return l