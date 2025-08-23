from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
queue = deque()

for _ in range(n):
    k = input().split()
    if len(k) == 2:
        queue.append(k[1])
    elif not queue:
        if k[0] == 'pop' or k[0] == 'front' or k[0] == 'back':
            print(-1)
        elif k[0] == 'size':
            print(0)
        elif k[0] == 'empty':
            print(1)
    elif k[0] == 'pop':
        print(queue.popleft())
    elif k[0] == 'size':
        print(len(queue))
    elif k[0] == 'empty':
        print(0)
    elif k[0] == 'front':
        print(queue[0])
    elif k[0] == 'back':
        print(queue[-1])

