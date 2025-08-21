import sys
input = sys.stdin.readline


def can(n):
    if n == 0:
        return "-"
    prev = can(n-1)
    return prev + (" " * (3 ** (n-1))) + prev
                
for line in sys.stdin:
    n = int(line)
    print(can(n))