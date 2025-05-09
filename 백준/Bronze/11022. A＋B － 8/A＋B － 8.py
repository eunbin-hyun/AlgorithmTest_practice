import sys

n = int(input())
k = []

for i in range(n):
    a,b = map(int, sys.stdin.readline().split())
    k.append([a,b])

for i in range(n):
    print(f"Case #{i+1}: {k[i][0]} + {k[i][1]} =",sum(k[i]))
