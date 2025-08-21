import sys
input = sys.stdin.readline

n, m, r = map(int, input().split())
graph = [[] for _ in range(n+1)]

for i in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
for v in range(1,n+1):
    graph[v].sort()

visited = [0]*(n+1)   
stack =[r]
cnt = 0

while stack:
    v = stack.pop()
    if visited[v] != 0:
        continue
    cnt += 1
    visited[v] = cnt
    for nxt in graph[v]:
        if visited[nxt] == 0:
            stack.append(nxt)
            
for i in range(1, n+1):
    print(visited[i])