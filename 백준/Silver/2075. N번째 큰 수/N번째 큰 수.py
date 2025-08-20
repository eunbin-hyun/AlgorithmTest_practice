import sys, heapq
input = sys.stdin.readline

heap = []
n = int(input())

if n > 100:
    for _ in range(n-100):
        X = list(map(int, input().split()))
    for _ in range(100):
        X = list(map(int, input().split()))
        for x in X:
            heapq.heappush(heap, -x)
else:
    for _ in range(n):
        X = list(map(int, input().split()))
        for x in X:
            heapq.heappush(heap, -x)
    
for _ in range(n):
    k = -heapq.heappop(heap)

print(k)
