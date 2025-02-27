def solution(numbers):
    answer = 0
    for i in numbers:
        answer += i
    answer = float( answer / len(numbers))
    return answer