import sys

ans = int(sys.stdin.readline())

for i in range(1,ans+1):
    total = (i*(i+1))//2
    if total == ans:
        n = i
        s = 0
        break
    elif total > ans:
        n = i
        s = (n*(n+1))//2 -ans
        break


if ans == 1:
    print(f"1/1")
elif n % 2 == 0:
    seg = n-s
    print(f"{seg}/{n-seg+1}")
else:
    seg = n-s 
    print(f"{n-seg+1}/{seg}")