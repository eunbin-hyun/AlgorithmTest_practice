from collections import deque

for t in range(1, 11): 
    n = int(input())
    arr = [list(map(int, input().split())) for i in range(n)]
    answer = 0

    for i in range(n):
        q = deque()
        # 한 열씩 체크
        for j in range(n):
            if arr[j][i] != 0:
                q.append(arr[j][i])
        if q:
            # 위쪽 s극(2) 없애기
            while True:
                k = q.popleft()
                if k == 1:
                    q.appendleft(k)
                    break
            # 아래쪽 n극(1) 없애기
            while True:
                k = q.pop()
                if k == 2:
                    q.append(k)
                    break
        # 교착 상태 세기
        if q:
            temp = []
            while q:
                k = q.popleft()
                if k == 1:
                    temp.append(1)
                else:
                    if temp:
                        answer +=1
                    temp = []
    print(f"#{t} {answer}")
