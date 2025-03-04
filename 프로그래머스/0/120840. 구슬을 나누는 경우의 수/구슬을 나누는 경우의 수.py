def solution(balls, share):
    answer = 0
    minus = balls - share
    
    def factorial(n):
        if n <= 1:
            return 1
        else:
            return n * factorial(n-1)

    answer = factorial(balls)/(factorial(minus)*factorial(share))
    return answer