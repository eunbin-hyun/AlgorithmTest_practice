n,b = map(int, input().split())
k = []

while n > 0:
    k.append(n % b)
    n = n // b
    
for i in range(len(k)-1,-1,-1):
    if 0<= k[i] <=9:
        num = k[i]
    else:
        num = chr(k[i]+ord('A')-10)
    print(num, end='')