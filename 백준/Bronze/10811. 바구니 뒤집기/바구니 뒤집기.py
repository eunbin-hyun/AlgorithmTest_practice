n,m = map(int, input().split())
b = [i for i in range(n+1)]
k = []

for i in range(m):
    k.append(input().split())
    
for i in range(m):
    start = int(k[i][0])
    end = int(k[i][1]) +1
    temp= b[start:end]
    b[start:end] = temp[::-1]
    
print(' '.join(map(str,b[1:])))