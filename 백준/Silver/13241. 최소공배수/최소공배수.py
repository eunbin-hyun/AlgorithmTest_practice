
A,B = map(int, input().split())

if A >= B:
    a = A
    b = B
else:
    a = B 
    b = A

while a % b > 0:
    if a % b != 0:
        tmp = a % b
        a = b
        b = tmp

if a % b == 0:
    print(A*B//b)