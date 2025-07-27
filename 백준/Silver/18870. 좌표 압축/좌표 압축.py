import sys
input = sys.stdin.readline

n = int(input())
X = list(map(int, input().split()))
X_sort = sorted(list(set(X)))

compress = {num :i for i, num in enumerate(X_sort) }
result = [compress[num] for num in X]
print(*result)