def solution(num, k):
    answer = -1
    num_list = list(map(int, str(num)))
    for i in num_list:
        if i == k:
            answer = num_list.index(i) + 1
    return answer