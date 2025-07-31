from collections import deque

n, k = map(int, input().split())
que = deque()

for i in range(1,n+1):
    que.append(i)

result = []

while n > len(result):
    for i in range(1,k+1):
        if n == len(result):
            break
        if i != k:
            q = que.popleft()
            que.append(q)
        else:
            q = que.popleft()
            result.append(q)

print("<", end="")
for i in range(n-1):
    print(result[i], end=", ")
print(result[-1], end="")
print(">")