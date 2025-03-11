def solution(arr):
    answer = 0
    x = 0

    while True:
        change = []
        for i in range(len(arr)):
            if arr[i]>=50 and arr[i]%2==0:
                change.append(int(arr[i]/2))
            elif arr[i]<50 and arr[i]%2==1:
                change.append(int(arr[i]*2 +1))
            else:
                change.append(arr[i])  
        
        if change == arr:
            return x
        
        x = x + 1
        arr = change
