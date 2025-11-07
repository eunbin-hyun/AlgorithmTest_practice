from collections import deque
T = int(input())

# 우, 하, 좌, 상
dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

for t in range(1, T+1):
    n = int(input())
    arr = [[0]*n for _ in range(n)]
    x,y = 0,0
    arr[x][y] = 1
    q = deque([])
    q.append((x,y))
    i = 0
    while q:
        x,y = q.popleft()
        cnt = 0
        while cnt <4:
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx < n and 0<= ny < n:
                if arr[nx][ny] == 0:
                    arr[nx][ny] = arr[x][y] +1
                    q.append((nx,ny))
                    break
                else:
                    i = (i+1)%4
                    cnt += 1
            else:
                i = (i+1)%4
                cnt += 1

    print(f"#{t}")
    for i in arr:
        print(' '.join(map(str, i)))