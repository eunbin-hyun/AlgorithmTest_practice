def solution(my_str, n):
    answer = []
    for i in range((len(my_str) + n - 1 )//n):
        answer.append(my_str[i*n:i*n+n])
    return answer