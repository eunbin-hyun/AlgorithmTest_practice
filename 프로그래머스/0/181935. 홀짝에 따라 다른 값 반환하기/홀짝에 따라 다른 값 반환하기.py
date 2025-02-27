def solution(n):
    answer = 0
    if n % 2 == 1:
        for i in range(n+1):
            if i % 2 == 1:
                answer += i
    else: 
        for j in range(n+1):
            if j % 2 == 0:
                answer += (j**2)
    return answer