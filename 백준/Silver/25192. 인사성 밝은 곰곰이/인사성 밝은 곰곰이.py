import sys
input = sys.stdin.readline

n = int(input())
cnt = 0
imt = set()

for _ in range(n):
    chat = input().strip()
    if chat == 'ENTER':
        cnt += len(imt)
        imt = set()
        continue
    imt.add(chat)

cnt += len(imt)
print(cnt)