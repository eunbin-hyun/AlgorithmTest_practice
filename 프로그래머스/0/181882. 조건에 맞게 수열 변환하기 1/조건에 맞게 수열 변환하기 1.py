def solution(arr):
    answer = arr
    for i in range(len(arr)):
        if arr[i] >= 50 and arr[i] % 2 == 0:
            answer[i] /= 2
        elif arr[i] < 50 and arr[i] % 2 == 1:
            answer[i] *= 2
    return answer