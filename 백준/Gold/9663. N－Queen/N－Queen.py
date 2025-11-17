n = int(input())

ans = 0
row = [0]*n

def is_promising(x):
    for i in range(x):
        # 같은 열 or 대각선에 있으면 False
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x-i):
            return False

    return True

def n_queens(x):
    global ans
    # 종료 조건 (해답 추가)
    if x == n:
        ans += 1
        return

    else:
        # 아직 다 못 놓았을 때
        for i in range(n):
            # [x.i]에 퀸을 놓겠다(임시)
            row[x] = i
            # 방금 둔 퀸이 앞에 퀸들과 충돌하는지 확인
            if is_promising(x):
                n_queens(x+1) # 괜찮으면 다음 행 진행
            # 안괜찮으면 무시하고 다음열(i+1) 시도

n_queens(0) # 0번째 행부터 시작
print(ans)