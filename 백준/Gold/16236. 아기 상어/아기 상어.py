from collections import deque

n = int(input())
array = [list(map(int,input().split())) for _ in range(n)]

# 탐색순서: 위, 왼, 아, 오
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def check_distance(x,y):
    """가까운 곳에 물고기 있는지 탐색.(거리 계산) array는 바꾸지 않는다"""
    visited = [[0]*n for _ in range(n)] #거리 계산
    q = deque()
    q.append((x,y))
    visited[x][y] = 1
    temp = []
    min_dist = None
    while q:
        x,y = q.popleft()
        cd = visited[x][y]
        # 이미 같은 거리 후보 찾았고, 더 먼칸이면 확장 중단
        if min_dist is not None and cd + 1 > min_dist:
            continue

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 지나갈수있는지(상어크기 이하만 통과)
            if 0 <= nx < n and 0<= ny < n and visited[nx][ny] == 0 and array[nx][ny] <= s_size:
                visited[nx][ny] = cd + 1  # ★ 거리 갱신 필수

                # 먹을수있는지
                if 0< array[nx][ny] < s_size:
                    if min_dist is None:
                        min_dist = visited[nx][ny]  # 최초 발견 거리 고정
                    if visited[nx][ny] == min_dist:
                        temp.append([nx,ny])
                # 아직 목표 거리 미정이면 계속 확장
                if min_dist is None:
                    q.append((nx, ny))
    return (temp, visited)

def eat_fish(g, fish):
    """가장 우선순위되는 물고기를 먹는다. array 업데이트"""
    g[0].sort()
    x,y = g[0][0]
    array[x][y] = 9
    visited = k[1]
    dis = visited[x][y]-1
    fish += 1
    return (x,y, dis, fish)

def size_up(x,y, fish, s_size):
    """몸집 키우기확인"""
    if fish == s_size:
        s_size += 1
        fish = 0
    return (x,y, fish, s_size)


result = 0
s_size = 2
fish = 0
while True:
    is_True = True
    # 상어 위치 찾기 
    for i in range(n):
        for j in range(n):
            if array[i][j] == 9:
                array[i][j] = 0
                k =check_distance(i,j)
                is_True = False
                if is_True == False:
                    break
        if is_True == False:
            break

    if k[0]:
        p=eat_fish(k, fish)
    # 못찾았으면 끝내기 
    else:
        break
    

    # 크기 키울수있는지 확인
    if p:
        x, y , dis, fish = p
        result += dis
        x,y, fish, s_size = size_up(x,y, fish, s_size)

print(result)

