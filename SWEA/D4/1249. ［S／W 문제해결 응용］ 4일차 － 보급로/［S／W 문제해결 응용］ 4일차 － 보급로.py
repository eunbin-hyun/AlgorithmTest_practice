from collections import deque
T = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x,y):
    q = deque()
    q.append((x,y))
    visited[x][y] = arr[x][y]
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x +dx[i]
            ny = y +dy[i]
            if 0<= nx < n and 0<= ny < n:
                if visited[nx][ny] == -1:
                    visited[nx][ny] = visited[x][y] + arr[nx][ny]
                    q.append((nx, ny))
                elif visited[nx][ny] > visited[x][y] + arr[nx][ny]:
                    visited[nx][ny] = visited[x][y] + arr[nx][ny]
                    q.append((nx, ny))

for test in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input())) for _ in range(n)]
    visited = [[-1]*n for _ in range(n)] #누적거리
    bfs(0,0)
    print(f"#{test} {visited[n-1][n-1]}")