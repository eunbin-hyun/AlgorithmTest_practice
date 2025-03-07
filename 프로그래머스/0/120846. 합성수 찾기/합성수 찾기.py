def solution(n):
    answer = 0
    for i in range(2, n+1):
        for j in range(2, i+1):
            if i / j == i // j != 1:
                answer += 1
                break
    return answer