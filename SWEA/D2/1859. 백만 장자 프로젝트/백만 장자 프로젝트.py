T = int(input())

for num in range(1,T+1):
    n = int(input())
    k = list(map(int, input().split()))
    buy = []
    result = 0
    maxval = max(k)
    
    for i in range(len(k)):
        if k[i] == maxval:
            if buy:
                for j in buy:
                    result += maxval - j
                buy = []
            if i+1 < len(k):
                maxval = max(k[i+1:])
        else:
            buy.append(k[i])
    
    print(f"#{num} {result}")    