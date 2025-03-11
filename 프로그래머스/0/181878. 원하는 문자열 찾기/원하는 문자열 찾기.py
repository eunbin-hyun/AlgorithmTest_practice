def solution(myString, pat):
    answer = 0
    i = myString.upper()
    j = pat.upper()
    
    if j in i:
        answer = 1
    return answer