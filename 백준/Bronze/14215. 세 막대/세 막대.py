import sys

a,b,c = map(int, sys.stdin.readline().split())
    
if max(a,b,c) < (a+b+c) - max(a,b,c):
    print(a+b+c)
else:
    max_num = (a+b+c) - max(a,b,c) -1
    print(max_num + (a+b+c) - max(a,b,c))
    