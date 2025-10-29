import heapq
n = int(input())

heap = []

for i in range(n):
    s, e = map(int, input().split())
    heapq.heappush(heap, (e, s))

end, start = heapq.heappop(heap)
cnt = 1

while heap:
    e, s = heapq.heappop(heap)
    if end > s:
        continue
    cnt += 1
    end, start = e, s

print(cnt)