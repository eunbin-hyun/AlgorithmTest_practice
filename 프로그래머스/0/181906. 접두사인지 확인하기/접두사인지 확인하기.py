def solution(my_string, is_prefix):
    pre = []
    answer = 0
    for i in range(len(my_string)):
        pre.append(my_string[0:i+1])
        if pre[i] == is_prefix:
            answer = 1
    return answer