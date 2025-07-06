import sys

A,B,V = map(int, sys.stdin.readline().split())
day = 0
m = 0
if V/A >100:
    day = (V-A)//(A-B)
    m = day*(A-B)
while m <= V:
    day+= 1 
    m += A
    if m >=V:
        break
    else:
        m -= B

print(day)
