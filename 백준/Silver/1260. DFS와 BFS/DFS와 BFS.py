import sys
from collections import deque
input = sys.stdin.readline

n, m, v = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(n+1):
    graph[i].sort()

qs = deque([v])
visited = [0] *(n+1)
cnt = 0

while qs:
    k = qs.pop()
    if visited[k]:
        continue
    
    cnt += 1
    visited[k] = cnt
    
    for i in graph[k][::-1]:
        if visited[i] == 0:
            qs.append(i)

for i in range(1, max(visited)+1):
    print(visited.index(i), end=" ")

qs = deque([v])
visited = [0] *(n+1)
cnt = 0

while qs:
    k = qs.popleft()
    if visited[k]:
        continue
    
    cnt += 1
    visited[k] = cnt
    
    for i in graph[k]:
        if visited[i] == 0:
            qs.append(i)

print()
for i in range(1, max(visited)+1):
    print(visited.index(i), end=" ")
