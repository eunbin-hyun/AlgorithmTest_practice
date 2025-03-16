def solution(num_list):
    answer = []
    k = sorted(num_list)
    for i in k:
        answer.append(i)
        if len(answer) == 5:
            break
    return answer