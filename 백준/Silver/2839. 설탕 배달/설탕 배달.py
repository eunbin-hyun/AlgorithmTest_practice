import sys
input = sys.stdin.readline

n = int(input())

cnt = n//5 + 1
k = cnt*5
result = 0

while True:
    if k == n:
        result = cnt
        break
    elif n == 3 or n==5:
        print(1)
        break
    elif n == 1 or n ==2 or n==4:
        print(-1)
        break
    elif k == cnt*3 and n%3 != 0:
        print(-1)
        break
    elif k > n:
        k -= 5
        cnt -= 1
    elif k < n :
        k += 3
        cnt += 1

if result !=0:
    print(result)