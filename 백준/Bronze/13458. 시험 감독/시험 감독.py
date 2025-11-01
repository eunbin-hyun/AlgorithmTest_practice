n = int(input())
arr = list(map(int, input().split()))
b, c = map(int, input().split())
result = n

for i in range(n):
    arr[i] -= b

for i in range(n):
    if arr[i] <= 0:
        continue
    elif arr[i]%c == 0:
        result += arr[i]//c
    else:
        result += arr[i]//c +1

print(result)