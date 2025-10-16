
arr = []
while True:
    a,b,c = map(int, input().split())
    if a == -1 and b == -1 and c == -1:
        break
    arr.append((a,b,c))

dp = [[[1 for _ in range(21)] for _ in range(21)] for _ in range(21)]


for a in range(1,21):
    for b in range(1,21):
        for c in range(1,21):
            if a<b and b<c:
                dp[a][b][c] = dp[a][b][c-1] + dp[a][b-1][c-1] - dp[a][b-1][c]
            else:
                dp[a][b][c] = dp[a-1][b][c] + dp[a-1][b-1][c] + dp[a-1][b][c-1] - dp[a-1][b-1][c-1]

result = 0
for a,b,c in arr:
    if a<=0 or b <= 0 or c <= 0:
        result = dp[0][0][0]
    elif a >20 or b>20 or c >20:
        result = dp[20][20][20]
    else:
        result = dp[a][b][c]
    print(f"w({a}, {b}, {c}) = {result}")