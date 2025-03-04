def solution(my_string):
    answer = []
    k = ''
    for i in range(len(my_string)):
        k = my_string[-i:]
        answer.append(k)
    answer.sort()
    return answer