def solution(sides):
    answer = 0
    a = 0
    for i in sides:
        if i > a:
            a = i
    
    if sides.index(a) == 0:
        if sides[0] < sides[1] + sides[2]:
            answer = 1
        else:
            answer = 2
    if sides.index(a) == 1:
        if sides[1] < sides[0] + sides[2]:
            answer = 1
        else:
            answer = 2
    if sides.index(a) == 2:
        if sides[2] < sides[1] + sides[0]:
            answer = 1
        else:
            answer = 2
    return answer