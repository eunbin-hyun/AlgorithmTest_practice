n = int(input())
k = []

for i in range(n):
    k.append(list(map(int, input().split())))
    
max_x = -10001
max_y = -10001
min_x = 10001
min_y = 10001

for x,y in k:
    max_x = max(x, max_x)
    max_y = max(y, max_y)
    min_x = min(x, min_x)
    min_y = min(y, min_y)
    
print((max_x - min_x)*(max_y - min_y))