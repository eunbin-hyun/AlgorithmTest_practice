from collections import deque
import sys

input = sys.stdin.readline
d = deque()

n = int(input())

for _ in range(n):
    k = list(input().split())
    if len(k) == 2:
        if k[0] == 'push_front':
            d.appendleft(k[1])
        else:
            d.append(k[1])
    elif not d:
        if k[0] == 'pop_front' or k[0] == 'pop_back' or k[0] == 'front' or k[0] == 'back':
            print(-1)
        elif k[0] == 'size':
            print(0)
        elif k[0] == 'empty':
            print(1)
    else:
        if k[0] =='pop_front':
            print(d.popleft())
        elif k[0] == 'pop_back':
            print(d.pop())
        elif k[0] == 'size':
            print(len(d))
        elif k[0] == 'empty':
            print(0)
        elif k[0] == 'front':
            print(d[0])
        elif k[0] == 'back':
            print(d[-1])