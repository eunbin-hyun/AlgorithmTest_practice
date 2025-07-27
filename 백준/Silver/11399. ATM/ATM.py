import sys
input = sys.stdin.readline

n = int(input())
line = list(map(int, input().split()))
line.sort()
d = [0]*(n+1)
result = 0

for i in range(n):
    result = result + line[i]
    d[i+1] = result

print(sum(d))