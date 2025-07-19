import sys
input = sys.stdin.readline

n = int(input())

k = list(int(input()) for i in range(n))
k.sort()

for i in range(n):
    print(k[i])