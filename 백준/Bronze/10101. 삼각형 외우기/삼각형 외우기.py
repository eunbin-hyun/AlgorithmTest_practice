import sys
angle = []

for _ in range(3):
    n = int(sys.stdin.readline())
    angle.append(n)
    
if min(angle) == 60 == max(angle):
    print("Equilateral")
elif sum(angle) == 180:
    if angle[0] == angle[1] or angle[1] == angle[2] or angle[2] == angle[0]:
        print("Isosceles")
    else:
        print("Scalene")
else:
    print("Error")
