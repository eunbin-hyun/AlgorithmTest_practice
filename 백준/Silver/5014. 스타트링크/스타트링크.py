from collections import deque

F,S,G,U,D  = map(int,input().split())
visited = [0]*(1000001)
queue = deque()

def bfs(f,s,g,u,d):
    queue.append(s)
    visited[s] = 1
    while queue:
        k = queue.popleft()
        for i in (u,-d):
            if 1<= k+i <= f and visited[k+i] == 0:
                queue.append(k+i)
                visited[k+i] = visited[k]+1
    return visited[g]


if bfs(F,S,G,U,D) == 0:
    print("use the stairs")
else:
    print(visited[G]-1)
