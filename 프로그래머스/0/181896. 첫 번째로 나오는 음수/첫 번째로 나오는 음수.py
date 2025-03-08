def solution(num_list):
    answer = 0
    for i in num_list:
        if i < 0:
            answer += num_list.index(i)
            break
    if num_list[0] >= 0 and answer == 0:
        answer = -1
    return answer