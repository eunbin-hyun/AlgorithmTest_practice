from collections import deque

T = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, arr, visited):
    queue = deque()
    queue.append((x,y))
    while queue:
        x,y = queue.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx < m and 0<= ny < n:
                if [nx,ny] in arr:
                    i = arr.index([nx,ny])
                    if visited[i] == False:
                        visited[i] = True
                        queue.append((nx,ny))


for _ in range(T):
    m,n,k = map(int, input().split())
    arr = []
    visited = [False]*k
    cnt = 0

    for _ in range(k):
        arr.append(list(map(int, input().split())))


    for i in range(k):
        x,y = arr[i]
        if visited[i] == False:
            bfs(x,y, arr, visited)
            cnt +=1
    print(cnt)
