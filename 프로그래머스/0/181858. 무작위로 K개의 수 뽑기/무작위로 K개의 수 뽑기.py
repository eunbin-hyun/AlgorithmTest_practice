def solution(arr, k):
    answer = []
    for i in arr:
        if i not in answer:
            answer.append(i)
    if len(answer) < k:
        for j in range(k - len(answer)):
            answer.append(-1)
    elif len(answer) > k:
        for j in range(len(answer) - k):
            answer.pop()
    return answer