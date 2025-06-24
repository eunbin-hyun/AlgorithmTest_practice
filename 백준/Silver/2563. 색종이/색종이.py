num = int(input())
k = []

for i in range(num):
    k.append(input().split())

arr = [[0]*100 for _ in range(100)]

for x,y in k:
    for i in range(int(x),int(x)+10):
        for j in range(int(y), int(y)+10):
            arr[i][j] = 1

cnt = 0 
for i in range(100):
    for j in range(100):
        if arr[i][j] == 1:
            cnt += 1
print(cnt)