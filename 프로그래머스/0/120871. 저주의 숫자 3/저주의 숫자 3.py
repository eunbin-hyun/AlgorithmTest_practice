def solution(n):
    num = 0
    count = 0
    while count < n:
        num += 1
        if num % 3 == 0 or "3" in str(num):
            continue
        else:
            count += 1
            
    return num