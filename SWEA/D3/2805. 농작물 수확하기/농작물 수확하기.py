T = int(input())

for t in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input())) for _ in range(n)]
    result = 0
    mid = (n-1)//2


    for i in range(n):
        # arr[i][j]
        # 위 쪽
        if i < mid:
            if i == 0:
                result += arr[i][mid]
            else:
                for j in range(mid-i, mid+i+1):
                    result += arr[i][j]
        # 가운데
        elif i == mid:
            for j in range(n):
                result += arr[i][j]
        # 아래
        else:
            if i == n-1:
                result += arr[i][mid]
            else:
                for j in range(i-mid, n-(i-mid)):
                    result += arr[i][j]

    print(f"#{t} {result}")
