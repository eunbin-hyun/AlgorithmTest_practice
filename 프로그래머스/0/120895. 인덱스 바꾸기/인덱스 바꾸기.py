def solution(my_string, num1, num2):
    answer = list(my_string)
    for i in range(len(my_string)):
        if num1 == i :
            temp = answer[num1]
        elif num2 == i :
            answer[num1] = answer[num2]
            answer[num2] = temp
    return ''.join(answer)