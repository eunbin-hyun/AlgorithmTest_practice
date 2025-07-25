import sys
input = sys.stdin.readline

m, n = map(int, input().split())
name_to_num = {}
num_to_name = {}

for i in range(m):
    name = input().strip()
    name_to_num[name] = i+1
    num_to_name[i+1] = name

for _ in range(n):
    k = input().strip()
    if k.isdigit():
        print(num_to_name[int(k)])
    else:
        print(name_to_num[k])
