def solution(my_string, letter):
    answer = ''
    list(my_string)
    for i in my_string:
        if i != letter:
            answer += i
    return answer