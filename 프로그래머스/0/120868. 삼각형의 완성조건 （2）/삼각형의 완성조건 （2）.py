def solution(sides):
    a = max(sides)
    b = min(sides)
    count = 0
    for i in range(2*a):
        if a > i and a < i+b:
            count += 1
        elif a <= i and i < a+b:
            count += 1
    return count