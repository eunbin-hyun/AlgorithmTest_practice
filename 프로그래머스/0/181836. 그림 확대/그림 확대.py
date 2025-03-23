def solution(picture, k):
    answer = []
    for i in picture:
        ans = ''
        for j in i:
            ans += j*k
        for l in range(k):
            answer.append(ans)
    return answer