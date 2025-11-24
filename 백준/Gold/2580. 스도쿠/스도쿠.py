
arr = [list(map(int, input().split())) for _ in range(9)]

# 0인 칸(빈 칸) 좌표 모으기
blanks = []
for i in range(9):
    for j in range(9):
        if arr[i][j] == 0:
            blanks.append((i, j))

def check(x,y,k):
    #가로 성립
    if k in set(arr[x]):
        return False

    #세로 성립
    for i in range(9):
        if arr[i][y] == k:
            return False

    #사각형 성립
    p = x//3
    q = y//3
    for i in range(0+p*3,3+p*3):
        for j in range(0+q*3, 3+q*3):
            if arr[i][j] == k:
                return False
    # 모든경우 가능할때 (많이 비어있으면 틀릴수있긴함)
    return True


def back(idx):
    # 모든 빈칸을 다 채웠으면 정답
    if idx == len(blanks):
        for row in arr:
            print(" ".join(map(str, row)))
        return True

    x,y = blanks[idx]

    for k in range(1, 10):
        if check(x,y,k):
            arr[x][y] = k # 선택
            if back(idx +1):# ★다음 빈칸까지도 올바르게 채워지는지 확인 (재귀 호출-> 마지막까지)
                return True  # 그렇다면 현재 단계도 성공이므로 더 종료
            arr[x][y] = 0 # 되돌리기

back(0)