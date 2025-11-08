
for test in range(1,11):
    dmp = int(input())
    k = list(map(int,input().split()))

    for _ in range(dmp):
        k.sort()
        k[0] += 1
        k[-1] -= 1
    k.sort()
    result = k[-1] - k[0]
    print(f"#{test} {result}")