import sys
from collections import Counter
input = sys.stdin.readline

n, m = map(int, input().split())
words = []

for _ in range(n):
    k = input().rstrip()
    if len(k) >= m:
        words.append(k)
    
count = Counter(words)
count = count.most_common()
count.sort(key = lambda x: (-x[1], -len(x[0]), x[0]))

for i in range(len(count)):
    print(count[i][0])
