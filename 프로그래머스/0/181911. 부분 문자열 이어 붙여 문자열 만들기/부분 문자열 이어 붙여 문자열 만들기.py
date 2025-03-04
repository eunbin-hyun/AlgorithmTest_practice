def solution(my_strings, parts):
    answer = ''
    for i in range(len(my_strings)):
        my_string = my_strings[i]
        s,e = parts[i]
        answer += my_string[s:e+1]
    return answer