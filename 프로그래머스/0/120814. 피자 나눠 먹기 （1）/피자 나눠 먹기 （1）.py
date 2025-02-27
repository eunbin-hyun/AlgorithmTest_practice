def solution(n):
    answer = 0
    if n % 7 == 0:
        i = 0
    else:
        i = 1
    answer = n // 7 + i
    return answer