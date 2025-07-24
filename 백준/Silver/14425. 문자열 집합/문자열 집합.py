import sys
input = sys.stdin.readline

n,m = map(int, input().split())
n_list = []
m_list = []
cnt = 0

for _ in range(n):
    n_list.append(input())
    
for _ in range(m):
    m_list.append(input())

for m_word in m_list:
    if m_word in n_list:
        cnt += 1
        
print(cnt)