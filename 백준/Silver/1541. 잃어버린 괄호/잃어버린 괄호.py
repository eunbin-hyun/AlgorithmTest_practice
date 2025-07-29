k = list(input().split('-'))
result = 0

for i in range(len(k)):
    if i == 0:
        p = list(map(int, k[i].split('+')))
        result += sum(p)
    else:
        p = list(map(int, k[i].split('+')))
        result -= sum(p)

print(result)
