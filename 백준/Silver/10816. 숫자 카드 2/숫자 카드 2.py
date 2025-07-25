import sys
input = sys.stdin.readline

n = int(input())
n_list = list(map(int, input().split()))
n_dic = {}
for i in n_list:
    if i in n_dic:
        n_dic[i] = n_dic[i] + 1 
    else:
        n_dic[i] = 1
        
m = int(input())
m_dic = list(map(int, input().split()))

for i in m_dic:
    if i in n_dic:
        print(n_dic[i], end=' ')
    else:
        print('0', end=' ')