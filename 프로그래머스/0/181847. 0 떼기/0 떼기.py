def solution(n_str):
    answer = ''
    count = 0
    for i in n_str:
        if i == '0':
            count += 1
        else:
            break
    answer = n_str[count:]
    return answer