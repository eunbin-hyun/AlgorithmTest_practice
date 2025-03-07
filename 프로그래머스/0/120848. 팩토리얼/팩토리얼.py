def solution(n):
    answer = 1
    count = 1
    if n > 2:
        for i in range(2, n):
            answer *= i
            count += 1
            if answer > n :
                count = count - 1
                break 
    elif n ==2:
        count = 2
        
    return count