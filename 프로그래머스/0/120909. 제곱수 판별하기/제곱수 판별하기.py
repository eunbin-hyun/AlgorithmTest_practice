def solution(n):
    i = 1
    while n >= i**2:
        if n == (i**2) :
            return 1
        i += 1
    return 2