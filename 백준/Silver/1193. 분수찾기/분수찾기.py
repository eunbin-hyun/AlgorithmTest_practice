import sys

ans = int(sys.stdin.readline())

for i in range(1,ans+1):
    total = (i*(i+1))//2
    if total >= ans:
        n = i
        s = (n*(n+1))//2 - ans
        break

if n % 2 == 0:
    print(f"{n - s}/{s + 1}")
else:
    seg = n-s 
    print(f"{s + 1}/{n - s}")