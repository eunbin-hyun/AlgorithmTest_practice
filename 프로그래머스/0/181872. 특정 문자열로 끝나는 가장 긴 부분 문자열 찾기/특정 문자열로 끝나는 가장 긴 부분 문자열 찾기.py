def solution(myString, pat):
    answer = myString[:len(myString)-myString[::-1].find(pat[::-1])]
    return answer