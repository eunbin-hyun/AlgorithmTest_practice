import sys
from collections import deque
imput = sys.stdin.readline

n, m, r = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n+1):
    graph[i].sort()

queue = deque([r])
visited = [0] *(n+1)
cnt = 0

while queue:
    k = queue.popleft()

    if visited[k]:
        continue
    cnt += 1
    visited[k] = cnt

    if graph[k]:
        for i in graph[k]:
            if visited[i] == 0:
                queue.append(i)

for i in range(1, n+1):
    print(visited[i])
