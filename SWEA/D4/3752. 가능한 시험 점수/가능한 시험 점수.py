T = int(input())

for test in range(1,T+1):
    n = int(input())
    scores = list(map(int, input().split()))
    possible = {0}
    for s in scores:
        new_score = set()
        for p in possible:
            new_score.add(p+s)
        possible = possible | new_score
    print(f"#{test} {len(possible)}")

