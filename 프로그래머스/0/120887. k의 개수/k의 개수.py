def solution(i, j, k):
    answer = 0
    for a in range(i,j+1):
        if str(k) in str(a):
            A = str(a)
            answer += A.count(str(k))
    return answer