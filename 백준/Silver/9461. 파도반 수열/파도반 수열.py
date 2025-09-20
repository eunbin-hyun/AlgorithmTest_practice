T = int(input())

for _ in range(T):
    n = int(input())
    dp =[0]*(n+1)
    for i in range(n+1):
        if i <= 3:
            dp[i] = 1
        elif i <= 5:
            dp[i] =2
        else:
            j = i-5
            dp[i] = dp[j] + dp[i-1]

    print(dp[n])
