n,m = map(int, input().split())
array = []

def back():
    if len(array) == m:
        print(*array)
        return
    
    for i in range(1, n+1):
        if array:
            if i < max(array):
                continue
            
        array.append(i)
        back()
        array.pop()

back()