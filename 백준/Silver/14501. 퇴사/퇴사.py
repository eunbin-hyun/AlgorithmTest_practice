n = int(input())
sc = []
for _ in range(n):
    sc.append(list(map(int, input().split())))

dp = [0]*n
if sc[0][0] <= n:
    dp[0] = sc[0][1]

for i in range(1,n):
    if i + sc[i][0] <= n:
        dp[i] = max(dp[i], sc[i][1])
        for j in range(0,i):
            if i >= sc[j][0] +j:
                dp[i] = max(dp[i], sc[i][1]+dp[j])

print(max(dp))