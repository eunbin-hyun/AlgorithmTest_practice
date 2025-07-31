from collections import deque
import sys
input = sys.stdin.readline

q = deque()
n = int(input())

for i in range(n):
    k = list(input().split())

    if len(k) == 2:
        q.append(k[1])
    elif k[0] == 'pop':
        if not q:
            print(-1)
        else:
            j = q.popleft()
            print(j)
    elif k[0] =='size':
        if q:
            print(len(q))
        else:
            print(0)
    elif k[0] == 'empty':
        if q:
            print(0)
        else:
            print(1)
    elif k[0] == 'front':
        if q:
            print(q[0])
        else:
            print(-1)
    elif k[0] == 'back':
        if q:
            print(q[-1])
        else:
            print(-1)

