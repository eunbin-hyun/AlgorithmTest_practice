n, k = map(int, input().split())

def factorial(a):
    ans = 1
    for i in range(2, a+1):
        ans *= i
    return ans

result = factorial(n)/(factorial(n-k)*factorial(k))

print(int(result))