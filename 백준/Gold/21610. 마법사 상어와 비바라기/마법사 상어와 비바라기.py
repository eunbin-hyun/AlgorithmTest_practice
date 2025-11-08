from collections import deque
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
# 첫 비바라기 (N, 1), (N, 2), (N-1, 1), (N-1, 2)에 비구름
cloud  = deque([(n - 1, 0), (n - 1, 1), (n - 2, 0), (n - 2, 1)])
temp = deque([])

# 0번 / 1~8번 이동 좌표 (대각선 방향 2,4,6,8)
dx = [0, 0, -1, -1, -1, 0, 1, 1, 1]
dy = [0, -1, -1, 0, 1, 1, 1, 0, -1]

for _ in range(m):
    d, s = map(int, input().split())

    # 1) 구름 d,s 만큼 이동
    for _ in range(len(cloud)):
        x, y = cloud.popleft()
        nx = (x + dx[d]*s)%n
        ny = (y + dy[d]*s)%n
        # 2) 구름위치 물 1 증가
        arr[nx][ny] += 1
        cloud.append((nx, ny))

    #4) 구름위치에 대각선 방향 물있는 바구니만큼 물 증가
    for x,y in cloud:
        cnt = 0
        for i in (2,4,6,8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if arr[nx][ny] >= 1:
                    cnt +=1
        arr[x][y] += cnt


    #5) 물 2 이상인 모든 칸 구름
    prev = set(cloud) # not in 시간 초과나니 set로 바꿔서!
    for i in range(n):
        for j in range(n):
            if arr[i][j] >= 2 and (i,j) not in prev:
                arr[i][j] -= 2
                temp.append((i,j))

    # 3) 이전구름 사라지고 새로 업데이트
    cloud = temp
    temp = deque([])

# 바구니에 들어있는 물의 합
result = 0
for i in range(n):
    for j in range(n):
        result += arr[i][j]

print(result)