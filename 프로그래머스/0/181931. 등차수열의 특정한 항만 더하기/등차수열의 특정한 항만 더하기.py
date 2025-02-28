def solution(a, d, included):
    answer = 0
    for i,j in enumerate(included):
        if (i == 0) and j:
            answer += a
            
        elif (i !=0) and j:
            answer += (a + d*i)
            
    return answer