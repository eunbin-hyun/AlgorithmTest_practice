n = int(input())
stair = [0] + [int(input()) for _ in range(n)] # 1번부터 맞추기
dp= [0]*(n+1)

if n == 1:
    print(stair[1])
    exit()
elif n == 2:
    print(stair[1] + stair[2])
    exit()

dp[1] = stair[1]
dp[2] = stair[1] + stair[2]

for i in range(3, n+1):
    dp[i] = max(dp[i-2], dp[i-3]+ stair[i-1]) + stair[i]

print(dp[n])