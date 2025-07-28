n = int(input())
money = list(map(int, input().split()))
city = list(map(int, input().split()))

result = money[0]*city[0]
i = 1
minnum = 0

while i+1 < n:
    if city[i] < city[minnum]:
        minnum = i
    result += money[i]*city[minnum]
    i += 1

print(result)