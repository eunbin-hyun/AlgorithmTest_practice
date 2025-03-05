def solution(numbers, k):
    answer = 0
    if (2*k) > len(numbers):
        numbers = numbers * (k*2 // len(numbers) + 1)
    
    answer = numbers[2*(k-1)]
    return answer