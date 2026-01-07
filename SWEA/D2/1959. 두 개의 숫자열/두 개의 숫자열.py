
t = int(input())

for T in range(1, t+1):
    A, B = map(int, input().split())
    ans = list()

    if A <= B:
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
    else:
        b = list(map(int, input().split()))
        a = list(map(int, input().split()))

    for i in range(abs(A-B)+1):
        answer = 0
        for j in range(len(a)):
            answer += a[j] * b[j+i]
        ans.append(answer)

    print(f"#{T} {max(ans)}")