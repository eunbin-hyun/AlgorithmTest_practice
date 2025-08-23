import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

v = [False] * (n+1)

stack = [1]
while stack:
    k = stack.pop()
    if v[k] == True:
        continue
    v[k] = True
    for i in graph[k]:
        stack.append(i)

print(v.count(True)-1)