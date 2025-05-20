import sys
n, m = map(int, input().split())
k = []
result = [0]*(n+1)

for i in range(n+1):
    result[i] = i
    
for i in range(m):
    k.append(sys.stdin.readline().strip().split())
    
for i in range(m):
    result[int(k[i][0])], result[int(k[i][1])] = result[int(k[i][1])], result[int(k[i][0
    ])]
        
for i in range(1,n+1):
    print(result[i], end=' ')
