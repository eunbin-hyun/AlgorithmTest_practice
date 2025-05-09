import sys

n = int(input())
k = []

for i in range(n):
    a,b = map(int, sys.stdin.readline().split())
    k.append([a,b])

for i in range(n):
    print(sum(k[i]))