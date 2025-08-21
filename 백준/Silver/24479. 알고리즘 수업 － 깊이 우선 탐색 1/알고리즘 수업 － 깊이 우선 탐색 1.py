import sys
input = sys.stdin.readline

n, m, r = map(int, input().split())

graph = [[] for i in range(n+1)]

for i in range(1,m+1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for v in range(1, n+1):
    graph[v].sort(reverse = True)
    
visited = [0] *(n+1)
cnt = 0
    
stack = [r]
while stack:
    v = stack.pop()
    if visited[v]:
        continue
    cnt += 1 
    visited[v] = cnt
    for nxt in graph[v]:
        if not visited[nxt]:
            stack.append(nxt)

for i in range(1, n+1):
    print(visited[i])
