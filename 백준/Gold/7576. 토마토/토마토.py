from collections import deque

m,n = map(int, input().split())
arr = []
visited = [[-1]*m for _ in range(n)]
queue = deque()

for _ in range(n):
    arr.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]


def bfs():
    for x in range(n):
        for y in range(m):
            if arr[x][y] == 1:
                queue.append((x,y))
                visited[x][y] = 0

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue   
            if arr[nx][ny] ==0 and visited[nx][ny] == -1:
                queue.append((nx,ny))
                visited[nx][ny] = visited[x][y] +1

bfs()

is_already = True
for i in range(n):
    for j in range(m):
        if arr[i][j] ==0:
            is_already = False
        elif arr[i][j] == -1:
            visited[i][j] = 0


is_True = True
result = -1
for i in range(n):
    for j in range(m):
        if visited[i][j] == -1:
            is_True = False
    k = max(visited[i])
    result = max(result, k)

if is_already:
    print(0)
elif is_True:
    print(result)
else:
    print(-1)