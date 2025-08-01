from collections import deque
import sys
input = sys.stdin.readline

dd = deque()

n = int(input())

for _ in range(n):
    k = list(map(int, input().split()))
    if k[0] == 1:
        dd.appendleft(k[1])
    elif k[0] == 2:
        dd.append(k[1])
    elif k[0] == 5:
        if dd:
            print(len(dd))
        if not dd:
            print(0)
    elif k[0] == 6:
        if dd:
            print(0)
        else:
            print(1)
    else:
        if not dd:
            print(-1)
        elif k[0] == 3:
            i = dd.popleft()
            print(i)
        elif k[0] == 4:
            i = dd.pop()
            print(i)
        elif k[0] == 7:
            print(dd[0])
        elif k[0] == 8:
            print(dd[len(dd)-1])

