from collections import deque

T = int(input())

dx = [-2, -2, -1, -1, 1, 1, 2, 2]
dy = [1, -1, 2, -2, 2, -2, 1, -1]

def bfs(I, nx, ny, gx, gy):
    arr = [[0]*I for _ in range(I)]
    queue = deque()
    queue.append((nx,ny))

    while queue:
        x, y = queue.popleft() #bfs!!
        if x == gx and y == gy:
            print(arr[gx][gy])
            break

        for i in range(8):
            nx = x+ dx[i]
            ny = y+ dy[i]
            if 0 <= nx < I and 0 <= ny < I:
                if arr[nx][ny] == 0: 
                    queue.append((nx,ny))
                    arr[nx][ny] = arr[x][y] +1


for _ in range(T):
    I = int(input())
    nx, ny = list(map(int, input().split()))
    gx,gy = list(map(int, input().split()))
    bfs(I, nx, ny, gx, gy)