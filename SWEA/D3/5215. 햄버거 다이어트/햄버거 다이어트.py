
T = int(input())

def back(idx, score, cal):
    global best
    # 1) 칼로리 초과 가지치기
    if cal > L:
        return
    # 2) 끝까지 본 경우
    if idx == N:
        if score > best:
            best = score
        return

    # 3) idx 선택
    s, k = arr[idx]
    back(idx + 1, score + s, cal + k)
    # 4) idx 미선택
    back(idx + 1, score, cal)


for test in range(1, T+1):
    # 재료의 수, 제한 칼로리
    N, L  = map(int, input().split())
    # (맛, 칼로리)
    arr = [tuple(map(int, input().split())) for _ in range(N)]
    best = 0

    # (인덱스, 맛의 합, 칼로리의 합)
    back(0, 0, 0)
    print(f"#{test} {best}")

