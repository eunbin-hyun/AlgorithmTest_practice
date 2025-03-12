def solution(strArr):
    answer = []
    for i in range(len(strArr)):
        k = strArr[i]
        if i % 2 == 0:
            answer.append(k.lower())
        else:
            answer.append(k.upper())
    return answer