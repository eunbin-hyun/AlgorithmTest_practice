n = int(input())

def hanoi(n, start, end, sub):
    if n == 1:
        print(start, end)
    else:
        hanoi(n-1, start, sub, end)
        print(start, end)
        hanoi(n-1, sub, end, start)

print(2**n-1)
hanoi(n, 1,3,2)