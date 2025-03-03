def solution(my_string, queries):
    answer = my_string
    for s,e in queries:
        ans1 = answer[s:e+1]
        ans2 = ''.join(reversed(ans1))
        answer = ''.join([answer[:s], ans2, answer[e+1:]])
    return answer