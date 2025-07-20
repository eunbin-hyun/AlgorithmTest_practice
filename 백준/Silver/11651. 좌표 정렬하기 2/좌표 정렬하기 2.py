import sys
input = sys.stdin.readline

n = int(input())
xy_list = []

for i in range(n):
    xy_list.append(list(map(int, input().split())))

xy_list= sorted(xy_list, key = lambda x: (x[1], x[0]))

for x,y in xy_list:
    print(x,y)