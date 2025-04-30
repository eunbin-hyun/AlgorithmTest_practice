n, x = map(int, input().split())
a = list(map(int, input().split()))
result = []

for i in a:
    if i < x:
        result.append(i)

for i in result:
    print(i, end= ' ')