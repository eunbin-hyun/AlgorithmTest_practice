import sys

A,B,V = map(int, sys.stdin.readline().split())
day = (V-A)//(A-B)
m = (A-B)*day
while m <= V:
    day+= 1 
    m += A
    if m >=V:
        break
    else:
        m -= B
print(day)
