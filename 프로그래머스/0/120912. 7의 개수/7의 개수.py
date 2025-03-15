def solution(array):
    answer = 0
    for i in array:
        if '7' in str(i):
            answer += str(i).count('7')
    return answer