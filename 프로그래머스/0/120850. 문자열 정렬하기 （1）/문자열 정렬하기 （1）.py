def solution(my_string):
    answer = []
    for i in my_string:
        if i in '1234567890':
            answer.append(int(i))
    answer.sort()
    
    return answer