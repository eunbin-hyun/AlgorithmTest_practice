import sys
input = sys.stdin.readline

S = input().strip()
q = int(input())


for _ in range(q):
    a, l, r = input().split()
    result = S[int(l):int(r)+1]
    print(result.count(a))