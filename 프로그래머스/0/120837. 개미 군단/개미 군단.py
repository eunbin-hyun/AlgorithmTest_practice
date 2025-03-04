def solution(hp):
    answer = 0
    i = hp // 5 
    hp = hp % 5
    j = hp // 3
    hp = hp % 3
    k = hp // 1
    answer = i + j + k
    return answer