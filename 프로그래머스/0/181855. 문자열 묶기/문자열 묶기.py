def solution(strArr):
    answer = []
    ans = []
    for i in strArr:
        ans.append(len(i))
    ans.sort()
    ans1 = set(ans)
    for j in ans1:
        answer.append(ans.count(j)) 
    return max(answer)