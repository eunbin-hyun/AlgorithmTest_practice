import sys
input = sys.stdin.readline

n = int(input())
k =[0]*10001
for i in range(n):
    k[int(input())] += 1

for i in range(len(k)):
    for j in range(k[i]):
        print(i)