num = int(input())
divs = list(map(int,input().split()))
divs.sort()

if num%2 ==0:
    result = divs[0]*divs[-1]
else:
    result = divs[num//2]**2
    
print(result)
