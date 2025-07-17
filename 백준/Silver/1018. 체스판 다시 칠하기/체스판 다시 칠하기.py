import sys
input = sys.stdin.readline
n,m = map(int, input().split())
check = []

for i in range(n):
    k = list(input().strip())
    check.append(k)
        
case1 = [[] for i in range(8)]
case2 = [[] for i in range(8)]
for i in range(8):
    for j in range(8):
        if i%2==0 and j%2==0:
            case1[i].append('W')
            case2[i].append('B')
        elif i%2==0 and j%2 != 0:
            case1[i].append('B')
            case2[i].append('W')
        elif j%2==0:
            case1[i].append('B')
            case2[i].append('W')
        else:
            case1[i].append('W')
            case2[i].append('B')

result = []
for i in range(n-7):
    for j in range(m-7):
        k = 0
        h = 0
        for I in range(8):
            for J in range(8):
                if check[I+i][J+j] != case1[I][J]:
                    k +=1
                if check[I+i][J+j] != case2[I][J]:
                    h +=1
        result.append(k)
        result.append(h)

print(min(result))