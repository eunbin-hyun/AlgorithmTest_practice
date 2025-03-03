def solution(x1, x2, x3, x4):
    answer = False
    y1 = True
    y2 = True
    if not x1 and not x2:
        y1 = False
    if not x3 and not x4:
        y2 = False
    if y1 and y2:
        answer = True
        
    return answer