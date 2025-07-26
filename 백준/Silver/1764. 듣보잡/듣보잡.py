import sys
input = sys.stdin.readline

n,m = map(int, input().split())
n_set = set()
m_set = set()
result = []

for _ in range(n):
    n_set.add(input().strip())

for _ in range(m):
    m_set.add(input().strip())

for i in n_set:
    if i in m_set:
        result.append(i)

result.sort()

print(len(result))

for k in result:
    print(k)