def solution(N, stages):
    answer = []
    for i in range(N+1):
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
        answer[cur_stage] = [cur_stage, cnt/i]

    answer.sort(key = lambda n: n[0])
    answer.remove([0,0])
    answer.sort(key = lambda n: n[1], reverse=True)
    
    l = []
    for i in range(len(answer)):
        l.append(answer[i][0])
    return l