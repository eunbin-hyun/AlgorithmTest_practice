a1, a2 = map(int, input().split())

c = int(input())
n0 = int(input())

answer = True
for n in range(n0, 101):
    if a1*n + a2 > c*n:
        answer = False
        
if answer == False:
    print(0)
else:
    print(1)