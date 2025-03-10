def solution(array, n):
    array.sort()
    closet = array[0]
    min_diff = abs(n - closet)
    
    for num in array:
        diff = abs(n - num)
        if diff < min_diff:
            closet = num
            min_diff = diff
        elif diff == min_diff and num < closet :
            closet = num
            
    return closet
    
