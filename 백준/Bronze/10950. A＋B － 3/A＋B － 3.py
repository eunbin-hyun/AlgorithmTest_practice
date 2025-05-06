n = int(input())
k = [0]*n
for i in range(n):
    k[i] = list(map(int, input().split()))

for i in range(n):
    print(sum(k[i]))