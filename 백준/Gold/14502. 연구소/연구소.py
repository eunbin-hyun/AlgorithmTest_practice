from collections import deque

n,m = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(n)]

# 빈칸과 바이러스를 각각 1차원 리스트에 모아두기
empty = []
virus = []
for r in range(n):
    for c in range(m):
        if lab[r][c] == 0:
            empty.append((r,c))
        elif lab[r][c] == 2:
            virus.append((r,c))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def spread(board):
    """현재 board에서 바이러스(2) 확산 (BFS)"""
    q = deque(virus) # 초기 바이러스 위치들
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 0:
                board[nx][ny] = 2
                q.append((nx, ny))
            
def count_safe(board):
    """안전 구역(0의 개수) 계산"""
    cnt = 0
    for r in range(n):
        # count(0)가 빠르고 간단
        cnt += board[r].count(0)
    return cnt

E = len(empty)
ans = 0

# 빈칸 인덱스 3개(i<j<k)를 뽑는 3중 for = 조합 구현
# board에 벽세우기 -> 확산 및 안전구역 계산(함수 호출)
for i in range(E):
    x1, y1 = empty[i]     # 첫 벽
    for j in range(i+1, E):
        x2, y2 = empty[j]     # 두 번째 벽
        for k in range(j+1, E):
            x3, y3 = empty[k]     # 세 번째 벽

            # 현재 조합에 대해 복사 후 벽 세우기
            board = [row[:] for row in lab]
            board[x1][y1] = 1
            board[x2][y2] = 1
            board[x3][y3] = 1

            # 바이러스 확산 및 안전구역 계산
            spread(board)
            safe = count_safe(board)
            if safe > ans:
                ans = safe

print(ans)
