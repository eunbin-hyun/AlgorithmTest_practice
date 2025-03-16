def solution(arr):
    answer = arr
    for i in range(len(arr)):
        if len(arr) <= (2**i):
            k = (2**i) % len(arr)
            break
    if k != 0:
        for j in range(k):
            answer.append(0)
    return answer