import sys
input = sys.stdin.readline
S = input().strip()
s_set = set()

for i in range(len(S)):
    for j in range(i+1, len(S)+1):
        s_set.add(S[i:j])   

print(len(s_set))