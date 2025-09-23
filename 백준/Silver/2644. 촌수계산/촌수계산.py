from collections import deque

n = int(input())
start, end = map(int, input().split())
m = int(input())
array =[[] for _ in range(n+1)]
visited = [0] *(n+1)
queue = deque()

for i in range(m):
    x, y = map(int, input().split())
    array[x].append(y)
    array[y].append(x) 

def bfs(array, s, visited):
    visited[s] = 0
    queue.append(s)
    while queue:
        k = queue.popleft()
        for i in array[k]:
            if i == end:
                return visited[k] + 1
            if not visited[i]:
                visited[i] = visited[k] + 1
                queue.append(i)

    return -1

    
print(bfs(array, start, visited))