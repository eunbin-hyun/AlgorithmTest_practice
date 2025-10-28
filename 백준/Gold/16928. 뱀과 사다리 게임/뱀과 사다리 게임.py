from collections import deque

n, m = map(int, input().split())

up = [list(map(int, input().split())) for _ in range(n)]
down = [list(map(int, input().split())) for _ in range(m)]
visited = [[0]*10 for _ in range(11)]
queue = deque([1])
is_true = False

while queue:
    k = queue.popleft()
    k = str(k)
    if len(k) == 1:
        x = 0
        y = int(k)
    else:
        x = int(k[0])
        y = int(k[1])

    # 주사위 굴리기
    for i in range(1,7):
        nk = int(k) +i
        if nk >100:
            continue
        # 100에 도달하면 리턴
        if nk == 100:
            result = visited[x][y] +1
            is_true = True
            break
        
        # 사다리나 뱀일 경우
        for j in range(n):
            if up[j][0] == nk:
                nk = up[j][1]
        for j in range(m):
            if down[j][0] == nk:
                nk = down[j][1]

        nk = str(nk)
        # visited를 위해 인덱스 변환
        if len(nk) == 1:
            nx = 0
            ny = int(nk)
        else:
            nx = int(nk[0])
            ny = int(nk[1])
        # append
        if visited[nx][ny] == 0:
            visited[nx][ny] = visited[x][y] +1
            queue.append(nk)
        
        # 100에 도달하면 리턴
        if nk == 100:
            result = visited[x][y] +1
            is_true = True
            break
    if is_true:
        break

print(result)