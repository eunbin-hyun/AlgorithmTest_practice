from collections import deque

n, k = map(int, input().split())
# 거리 최소 시간 배열 !!
visited = [-1]*(100001)
visited[n] = 0

def bfs(now, end):
    queue = deque()
    queue.append(now)
    cnt = 0
    while queue:
        x = queue.popleft()
        if x == k:
            return visited[x]
        for nx in (x-1, x+1, 2*x):
            # nx가 조건 성립 때만 visited 업데이트(점위치제한 & 첫 시간)
            if 0 <= nx <= 100000 and visited[nx] == -1:
                visited[nx] = visited[x] + 1
                queue.append(nx)
        
print(bfs(n,k))