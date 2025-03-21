def solution(numlist, n):
    answer = []
    gap = []
    for i in numlist:
        gap.append([abs(i-n), i])
    gap.sort()
    
    for j in range(1,len(numlist)):
        if gap[j-1][0] == gap[j][0]:
            gap[j-1][1] ,gap[j][1] = gap[j][1] ,gap[j-1][1]
            
    for k in range(len(numlist)):
        answer.append(gap[k][1])
    return answer