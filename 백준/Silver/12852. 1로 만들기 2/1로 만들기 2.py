n = int(input())

d = [1000001]*(n+1)
d[0], d[1] = 0, 0

for i in range(2, n+1):
    if d[i-1] != 1000001:
        d[i] = min(d[i-1]+1, d[i])
    if i%2 ==0 and d[i//2] != 1000001:
        d[i] = min(d[i//2]+1, d[i])
    if i%3 == 0 and d[i//3] != 1000001:
        d[i] = min(d[i//3]+1, d[i])
print(d[n])

k = n
print(k, end=" ")

while k > 1:
    if k%3 == 0 and d[k//3] == d[k]-1:
        k //= 3
        print(k, end =" ")
    elif k%2 == 0 and d[k//2] == d[k]-1:
        k //= 2
        print(k, end =" ")
    elif d[k-1] == d[k]-1:
        k -= 1
        print(k, end =" ")