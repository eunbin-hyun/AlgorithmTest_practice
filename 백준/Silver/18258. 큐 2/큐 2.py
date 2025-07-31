from collections import deque
import sys
input = sys.stdin.readline

k = []
q = deque()
n = int(input())

for _ in range(n):
    kk = list(input().split())
    k.append(kk)

for i in range(n):
    if len(k[i]) == 2:
        q.append(k[i][1])
    elif k[i][0] == 'pop':
        if not q:
            print(-1)
        else:
            j = q.popleft()
            print(j)
    elif k[i][0] =='size':
        if q:
            print(len(q))
        else:
            print(0)
    elif k[i][0] == 'empty':
        if q:
            print(0)
        else:
            print(1)
    elif k[i][0] == 'front':
        if q:
            print(q[0])
        else:
            print(-1)
    elif k[i][0] == 'back':
        if q:
            print(q[-1])
        else:
            print(-1)

