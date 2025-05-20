import sys
n, m = map(int, input().split())
k = []
result = [0]*(n+1)

for i in range(m):
    k.append(sys.stdin.readline().strip().split())
    
for i in range(m):
    for j in range(int(k[i][0]), int(k[i][1])+1):
        result[j] = int(k[i][2])
        
for i in range(1,n+1):
    print(result[i], end=' ')