import sys
input = sys.stdin.readline

n = int(input())
cards = set(map(int, input().split()))
m = int(input())
check = list(map(int, input().split()))

for c in check:
    if c in cards:
        print(1, end=' ')
    else:
        print(0, end=' ')
