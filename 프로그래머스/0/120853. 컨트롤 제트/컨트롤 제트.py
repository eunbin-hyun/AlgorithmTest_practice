def solution(s):
    answer = 0
    k = s.split()
    
    for i in range(len(k)) :
        if k[i] != 'Z':
            answer += int(k[i])
        elif k[i] == 'Z':
            answer -= int(k[i-1])
    return answer