from collections import deque

n,m = map(int, input().split())
array = []

for i in range(n):
    k = input()
    array.append([])
    for j in k:
        array[i].append(int(j))

q = deque()

# 동서남북
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def bfs(x,y):
    if array[x][y] == 1:
        array[x][y] = 1
        q.append((x,y))
        
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny <0 or ny >=m:
                continue
            elif array[nx][ny] == 1:
                array[nx][ny] = array[x][y] +1
                q.append((nx,ny))
    return array[n-1][m-1]
    
print(bfs(0,0))
