from collections import deque
m,n,h = map(int, input().split())
array = []

for i in range(h):
    array.append([])
    for j in range(n):
        array[i].append(list(map(int, input().split())))

dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]


queue = deque()

for i in range(h):
    for j in range(n):
        for k in range(m):
            if array[i][j][k] == 1:
                queue.append((i,j,k))
while queue:
    z,y,x = queue.popleft()
    for i in range(6):
        nx = x + dx[i]
        ny = y + dy[i]
        nz = z + dz[i]
        if nx<0 or nx>=m or ny<0 or ny>=n or nz<0 or nz>=h:
            continue
        if array[nz][ny][nx] == 0:
            array[nz][ny][nx] = array[z][y][x] +1
            queue.append((nz,ny,nx))


result = False
max_value = -2
for i in range(h):
    for j in range(n):
        for k in range(m):
            if array[i][j][k] == 0:
                result = True
            max_value = max(array[i][j][k], max_value)


if result == True:
    print(-1)
elif max_value == 1:
    print(0)
else:
    print(max_value-1)