import sys
input = sys.stdin.readline

n = int(input())
tree = []
tree_temp = []

for _ in range(n):
    tree.append(int(input()))

for i in range(1,n):
    tree_temp.append(tree[i]- tree[i-1])

tree_tp = list(set(tree_temp))
result = 1000000000
for i in range(len(tree_tp)):
    a = tree_tp[i]
    k = min(tree_temp)
    while k != 0:
        temp = a % k
        a = k
        k = temp
    result = min(a, result)

cnt = 0
for i in range(len(tree_temp)):
    if tree_temp[i] > result:
        cnt += tree_temp[i] // result -1
    
print(cnt)