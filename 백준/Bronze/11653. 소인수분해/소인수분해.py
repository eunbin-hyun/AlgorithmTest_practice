N = int(input())
num = 2

while N > 1:
    if N%num ==0:
        print(num)
        N = N//num
    else:
        num += 1 