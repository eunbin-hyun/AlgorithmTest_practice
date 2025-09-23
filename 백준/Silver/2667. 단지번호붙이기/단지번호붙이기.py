from collections import deque
visited = []
n = int(input())

for i in range(n):
    visited.append(list(map(int, input())))

q = deque()

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
result = []

def bfs(x,y):
    cnt = 1
    q.append((x,y))
    visited[x][y] = 0
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx <0 or nx>=n or ny<0 or ny >= n:
                continue
            elif visited[nx][ny] == 1:
                visited[nx][ny] = 0
                q.append((nx,ny))
                cnt +=1
    result.append(cnt)
    return True
            
            
ans = 0
for i in range(n):
    for j in range(n):
        if visited[i][j] == 1:
            if bfs(i,j) == True:
                ans +=1
print(ans)
result.sort()

for i in result:
    print(i)