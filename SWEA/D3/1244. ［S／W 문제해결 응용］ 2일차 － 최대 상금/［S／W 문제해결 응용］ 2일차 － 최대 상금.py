T = int(input())

for test in range(1, T+1):
    k, n = input().split()
    n = int(n)
    L = len(k)

    # 같은 레벨에서 중복 상태 제거하며 레벨(BFS) 진행
    cur = {k}
    for _ in range(n): # n번 교환 반복
        nxt = set()
        for s in cur: # cur에 대해 모든 경우의 수 교환하기
            arr = list(s)
            for i in range(L-1):
                for j in range(i+1, L):
                    b = arr[:]
                    b[i], b[j] = b[j], b[i]
                    nxt.add(''.join(b))
        # 다음 레벨로(이 레벨만 남게됨 cur이라는 set에)
        cur = nxt
            
    # n번 교환한 것 중에 최대값
    answer = max(cur)   # 자리수가 같기 때문에 문자임에도 max비교 맞음
    print(f"#{test} {answer}")
