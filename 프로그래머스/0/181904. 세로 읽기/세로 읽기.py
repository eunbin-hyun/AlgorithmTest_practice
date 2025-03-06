def solution(my_string, m, c):
    answer = ''
    ans = []
    for i in range(0, len(my_string)//m):
        ans.append(my_string[i*m: i*m+m])
        answer += ans[i][c-1:c]
    return answer