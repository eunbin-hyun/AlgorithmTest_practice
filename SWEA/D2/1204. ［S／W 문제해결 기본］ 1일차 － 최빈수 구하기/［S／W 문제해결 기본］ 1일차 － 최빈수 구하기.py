T = int(input())
for _ in range(1,T+1):
    test = int(input())
    score = list(map(int, input().split()))
    table = [0]*101
    for i in score:
        table[i] += 1
    cnt = -1
    result = -1
    for i in range(len(table)):
        if table[i] >= cnt:
            cnt = table[i]
            result = i
    print(f"#{test} {result}")