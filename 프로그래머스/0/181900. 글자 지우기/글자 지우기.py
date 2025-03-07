def solution(my_string, indices):
    answer = ''
    indices.sort(reverse = True)
    my_string = list(my_string)
    for i in indices:
        del my_string[i]
    answer = ''.join(my_string)
    return answer