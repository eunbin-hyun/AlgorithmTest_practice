import sys
input = sys.stdin.readline

n, k  = map(int, input().split())
coins = []
result = 0

for _ in range(n):
    coins.append(int(input()))

for i in range(n-1, -1, -1):
    result += k//coins[i]
    k %= coins[i]

print(result)