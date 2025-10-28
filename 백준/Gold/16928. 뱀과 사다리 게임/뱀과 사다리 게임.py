from collections import deque

n, m = map(int, input().split())

up = [list(map(int, input().split())) for _ in range(n)]
down = [list(map(int, input().split())) for _ in range(m)]
visited = [-1 for _ in range(101)]
queue = deque([1])
visited[1] = 0

is_true = False

while queue:
    k = queue.popleft()
    # 주사위 굴리기
    for i in range(1,7):
        nk = k +i
        if nk >100:
            continue

        # 사다리나 뱀일 경우
        for j in range(n):
            if up[j][0] == nk:
                nk = up[j][1]
        for j in range(m):
            if down[j][0] == nk:
                nk = down[j][1]

        if visited[nk] == -1:
            visited[nk] = visited[k] +1
            queue.append(nk)
        
        # 100에 도달하면 리턴
        if nk == 100:
            is_true = True
            break
    if is_true:
        break

print(visited[100])
