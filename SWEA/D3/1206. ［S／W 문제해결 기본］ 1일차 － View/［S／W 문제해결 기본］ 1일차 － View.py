
for testcase in range(1, 11):
    n = int(input())
    build = list(map(int, input().split()))
    result = 0
    
    for i in range(2,n-2):
        high = max(build[i-2], build[i-1], build[i+1], build[i+2])
        if high < build[i]:
            result += build[i] - high
            
    print(f"#{testcase} {result}")