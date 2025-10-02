n,m = map(int, input().split())
array = []

def back():
    if len(array) == m:
        print(*array)
        return # (1) 조건을 만족하면 더 깊이 안들어가고 종료

    for i in range(1, n+1):
        array.append(i)
        back()  # (2) 재귀 호출
        array.pop()
    return    # (3) 함수 끝났음을 명시

back()