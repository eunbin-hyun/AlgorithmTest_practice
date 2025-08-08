a, b = map(int, input().split())
c, d = map(int, input().split())

A, B = a*d + c*b , b*d
real_A, real_B = A, B

def gcd(A,B):
    while B != 0:
        A, B = B, A % B
    return A

result= gcd(A,B)
print(real_A//result , real_B//result)