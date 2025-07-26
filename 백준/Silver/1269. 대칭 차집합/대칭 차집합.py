import sys
input = sys.stdin.readline

a_len,b_len = map(int, input().split())
a = set(map(int, input().split()))
b = set(map(int, input().split()))
cnt = 0

for i in a:
    if i not in b:
        cnt += 1

for j in b:
    if j not in a:
        cnt += 1

print(cnt)