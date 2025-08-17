T = int(input())

for _ in range(T):
    n, m = map(int, input().split())

    def factorial(a):
        ans = 1
        for i in range(2, a+1):
            ans *= i
        return ans

    result = factorial(m)/(factorial(m-n)*factorial(n))

    print(int(result))