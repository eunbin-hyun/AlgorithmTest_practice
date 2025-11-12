from collections import deque

T = int(input())

for test in range(1,T+1):
    n, k = map(int, input().split())
    box = deque(list(input()))
    total = set()
    temp = []

    # 회전 n//4 만큼
    for _ in range(n//4):
        # box 길이 만큼 움직이기
        for _ in range(n):
            a = box.popleft()
            temp.append(a)
            box.append(a)
            if len(temp) == n//4:
                total.add(''.join(temp))
                temp = []
        # 회전
        a = box.popleft()
        box.append(a)

    result = []
    ans = 0 # 임시저장
    cnt = 0
    # 16진수 변환
    for i in total:
        for j in i:
            cnt += 1
            if j.isdigit():
                ans += int(j)*(16**(n//4-cnt))
            else:
                ans += (ord(j)- ord('A') + 10)*(16**(n//4-cnt))

            # 생성하는 수 업데이트, 리셋
            if cnt == n//4:
                result.append(ans)
                cnt = 0
                ans = 0
    result.sort(reverse = True)
    print(f"#{test} {result[k-1]}")
