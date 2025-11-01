n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [False] * n
answer = 1e9

def back(idx, cnt):
    global answer

    # 팀에 n/2명이 선택되면 능력 계산
    if cnt == n//2:
        start, link = 0, 0
        for i in range(n):
            for j in range(i+1, n): # 각 쌍을 한 번만
                if visited[i] and visited[j]:
                    start += arr[i][j] + arr[j][i]
                elif not visited[i] and not visited[j]:
                    link += arr[i][j] + arr[j][i]
        answer = min(answer, abs(start - link))
        

    # 백트래킹으로 조합 뽑기
    for i in range(idx, n):
        if not visited[i]:
            visited[i] = True   # i번을 스타트 팀에 넣어본다
            back(i+1, cnt +1)   # 다음 사람도 뽑아보러 탐색
            visited[i] = False  # 다시 되돌려서 다른경우 시도

# 0번은 스타트팀으로 고정
visited[0] = True
back(1,1)
print(answer)