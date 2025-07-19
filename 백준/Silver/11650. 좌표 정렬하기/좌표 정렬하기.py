import sys
input = sys.stdin.readline

n = int(input())
xy_list = []

for i in range(n):
    xy_list.append(list(map(int, input().split())))
    
xy_list.sort()

for x,y in xy_list:
    print(x,y)