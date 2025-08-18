from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
A = deque(map(int, input().split()))
B = deque(map(int, input().split()))
m = int(input())
C = deque(map(int, input().split()))

queue = deque()

for i in range(n):
    if A[i] == 0:
        queue.append(B[i])
for c in C:
    queue.appendleft(c)

for _ in range(m):
    k = queue.pop()
    print(k, end=" ")
