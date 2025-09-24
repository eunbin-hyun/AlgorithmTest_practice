from collections import deque
n = int(input())

array = []
for _ in range(n):
    array.append(list(map(int, input().split())))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x,y):
    visited[x][y] = 0
    queue.append((x,y))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<n:
                if visited[nx][ny] == 1:
                    visited[nx][ny] = 0
                    queue.append((nx, ny))
    return True
    
result = []
max_value = 0
for i in range(n):
    for j in range(n):
        max_value = max(array[i][j], max_value)

for h in range(max_value+1):
    ans = 0
    visited = [[0]*n for _ in range(n)]
    queue = deque()
    for i in range(n):
        for j in range(n):
            if array[i][j] > h:
                visited[i][j] =1
    for i in range(n):
        for j in range(n):
            if visited[i][j] ==1:
                if bfs(i,j) == True:
                    ans +=1
    result.append(ans)

print(max(result))