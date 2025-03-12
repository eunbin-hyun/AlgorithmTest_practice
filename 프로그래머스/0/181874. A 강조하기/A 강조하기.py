def solution(myString):
    answer = ''
    for i in myString:
        if i in "aA":
            answer += "A"
        else:
            answer += i.lower()
    return answer