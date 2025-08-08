import sys, math
input = sys.stdin.readline

n = int(input())
tree = []
diff = []

for _ in range(n):
    tree.append(int(input()))

for i in range(1,n):
    diff.append(tree[i]- tree[i-1])

g = diff[0]
for d in diff[1:]:
    g = math.gcd(g, d)

cnt = 0
for d in diff:
    cnt += d // g -1
print(cnt)