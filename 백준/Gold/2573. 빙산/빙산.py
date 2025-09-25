from collections import deque

n,m = map(int, input().split())
array =[list(map(int, input().split())) for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def count_components():
    """현재 array를 바꾸지 않고, 빙산(>0) 컨포넌트 수만 셈"""
    visited = [[False]*m for _ in range(n)]
    def bfs(sx, sy):
        q = deque([(sx, sy)])
        visited[sx][sy] = True
        while q:
            x, y = q.popleft()
            for k in range(4):
                nx, ny = x + dx[k], y + dy[k]
                if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and array[nx][ny] > 0:
                    visited[nx][ny] = True
                    q.append((nx, ny))

    comp = 0
    for i in range(n):
        for j in range(m):
            # 아직 방문 안 했고 빙산이 있는 칸 처음 발견하면
            if array[i][j] > 0 and not visited[i][j]:
                comp += 1           # 새로운 덩어리 발견
                if comp >= 2:
                    return comp     # 두 개 이상이면 바로 반환
                bfs(i,j)            # 같은 덩어리의 모든 칸 방문 처리
    return comp

def compute_melt():
    """각 칸이 이번 해 동안 얼만큼 녹는지(0~4) 계산해서 반환. array는 건드리지 않음"""
    melt = [[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if array[i][j] >0:
                cnt = 0
                for k in range(4):
                    ni, nj = i + dx[k], j +dy[k]
                    if 0<= ni < n and 0 <= nj < m and array[ni][nj] == 0:
                        cnt += 1
                melt[i][j] = cnt
    return melt

def apply_melt(melt):
    """계산된 melt를 한 번에 적용. 전부 녹았으면 True 반환"""
    all_zero = True
    for i in range(n):
        for j in range(m):
            # 녹이기 적용
            if array[i][j] > 0:
                array[i][j] = max(0, array[i][j] - melt[i][j])
            # 녹인 후 all_zero 확인
            if array[i][j] >0:
                all_zero = False
    return all_zero


year = 0
while True:
    # 1) 이번 해 녹는 양 계산 (array를 바꾸지 않음)
    melt = compute_melt()

    # 2) 한 번에 적용
    year += 1
    all_melted = apply_melt(melt)
    if all_melted:          # 끝까지 분리 안 되고 녹음
        print(0)
        break

    # 3) 적용 후 분리됐나?
    if count_components() >= 2:
        print(year)
        break