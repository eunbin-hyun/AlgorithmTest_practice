import sys
input = sys.stdin.readline
from collections import deque

m, n = map(int, input().split())
name_index = {}
dp = deque()

for i in range(m):
    name = input().strip()
    dp.append(name)
    name_index[name] = i+1
    

for _ in range(n):
    k = input().strip()
    if k.isdigit():
        print(dp[int(k)-1])
    else:
        print(name_index[k])
