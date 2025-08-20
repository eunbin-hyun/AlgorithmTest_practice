import sys
input = sys.stdin.readline
import heapq

heap = []
n = int(input())

for _ in range(n):
    x = int(input())
    if x == 0:
        if heap:
            print(heapq.heappop(heap)[1])
        else:
            print(0)
    else:
        if x > 0:
            heapq.heappush(heap, (x,x))
        else:
            heapq.heappush(heap, (-x, x))
