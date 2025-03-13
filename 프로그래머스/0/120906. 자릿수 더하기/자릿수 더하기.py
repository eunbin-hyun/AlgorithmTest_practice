def solution(n):
    answer = 0
    num = str(n)
    for i in num:
        answer += int(i)
    return answer