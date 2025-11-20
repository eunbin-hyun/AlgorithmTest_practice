T = int(input())


def is_promising(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x-i):
            return False

    return True

def n_queen(x):
    global ans

    if x == n:
        ans += 1
        return

    else:
        for i in range(n):
            # 행(x), 열(i)에 퀸을 놓겠다
            row[x] = i
            if is_promising(x):
                n_queen(x+1) # 괜찮으면 다음행 진행

for test in range(1, T+1):
    n = int(input())
    ans = 0
    row = [0]*n
    n_queen(0)
    print(f"#{test} {ans}")