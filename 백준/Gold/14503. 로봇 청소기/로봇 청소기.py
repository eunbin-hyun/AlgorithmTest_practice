from collections import deque

n,m = map(int, input().split())
r,c,d = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]

# 방향: 북, 동, 남, 서 (시계)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(sx, sy, sdir):
    q = deque()
    q.append((sx, sy, sdir))

    while q:
        x, y, dir = q.popleft()
        # 1번 현재 칸 청소 (방문 표시)
        if array[x][y] == 0 and visited[x][y] == 0:
            visited[x][y] = 1
        cnt = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx <n and 0<= ny <m and array[nx][ny] == 0 and visited[nx][ny] == 0:
                cnt += 1

        # 주변 4칸 중 청소 안 된 빈칸이 없는 경우 후진
        if cnt == 0:
            nx = x - dx[dir]
            ny = y - dy[dir]
            if 0<= nx <n and 0<= ny <m and array[nx][ny] == 0:
                q.append((nx, ny, dir))
                continue
            # 뒤쪽이 벽이라 가지 못하면 중단
            else:
                break
        # 청소 안 된 빈칸이 있는경우 반시계 90도 회전
        else:
            for i in range(4):
                dir -= 1
                if dir == -1:
                    dir = 3
                nx = x + dx[dir]
                ny = y + dy[dir]
                if 0<= nx <n and 0<= ny <m and array[nx][ny] == 0 and visited[nx][ny] == 0:
                    q.append((nx, ny, dir))
                    break

bfs(r,c,d)
result = 0
for i in range(n):
    for j in range(m):
        if visited[i][j] == 1:
            result += 1
print(result)

