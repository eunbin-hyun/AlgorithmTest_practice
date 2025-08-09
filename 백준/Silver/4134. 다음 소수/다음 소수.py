import sys, math
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    k = int(input())
    if k <= 2:
        result = 2
    else:
        i = k-1
        while True:
            is_True = True
            i += 1
            for j in range(2, int(math.sqrt(i))+1):
                if i % j == 0:
                    is_True = False
                    break
            if is_True == True:
                result = i
                break
    print(result)