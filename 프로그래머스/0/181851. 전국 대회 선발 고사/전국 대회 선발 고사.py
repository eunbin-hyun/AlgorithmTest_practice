def solution(rank, attendance):
    answer = 0
    ranking = []
    for i in range(len(rank)):
        if attendance[i]:
            ranking.append([rank[i],i])
    ranking.sort(key = lambda x:x[0])
    answer = 10000 * ranking[0][1] + 100 *ranking[1][1] + ranking[2][1]
    return answer