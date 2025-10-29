n = int(input())
sc = []
for _ in range(n):
    sc.append(list(map(int, input().split())))

dp = [0]*n

for i in range(n):
    if i + sc[i][0] <= n:
        dp[i] = max(dp[i], sc[i][1])
        for j in range(0,i):
            if i >= sc[j][0] +j:
                dp[i] = max(dp[i], sc[i][1]+dp[j])

print(max(dp))