def solution(array):
    array.sort()
    b = int(len(array)) // 2
    answer = array[b]
    return answer