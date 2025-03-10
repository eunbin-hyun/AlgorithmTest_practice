def solution(num_list):
    answer = 0
    ans1 = 0
    ans2 = 0
    for i in num_list[::2]:
        ans1 += i
    for j in num_list[1::2]:
        ans2 += j
        
    if ans1 > ans2:
        answer = ans1
    else:
        answer = ans2
    
    return answer