def solution(arr):
    answer = []
    ans = []
    for i in range(len(arr)):
        if arr[i] == 2:
            ans.append(i)
    if ans:
        a = min(ans)
        b = max(ans)
    else:
        return [-1]
    
    answer += arr[a:b+1]
    return answer