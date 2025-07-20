import sys
input = sys.stdin.readline

n = int(input())
dict_list = []

for i in range(n):
    dict_list.append(input().strip())


dict_list.sort()
dict_list.sort(key = lambda x : len(x))
result = []

for i in dict_list:
    if i not in result:
        result.append(i)

for i in result:
    print(i)