def solution(intStrs, k, s, l):
    answer = []
    ans = ''

    for i in range(len(intStrs)):
        ans = intStrs[i]
        if int(ans[s:s+l]) > k:
            answer.append(int(ans[s:s+l]))
    return answer