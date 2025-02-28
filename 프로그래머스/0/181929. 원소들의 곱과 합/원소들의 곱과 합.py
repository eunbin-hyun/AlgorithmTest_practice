def solution(num_list):
    answer = 0
    max_r = 1
    sum_r = 0
    for i in num_list:
        max_r *= i
        sum_r += i
    if max_r < (sum_r)**2:
        answer = 1
    return answer