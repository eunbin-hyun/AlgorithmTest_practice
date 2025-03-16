def solution(polynomial):
    answer = []
    ans_x = 0
    ans_num = 0
    polys = polynomial.split(" + ")
    for poly in polys:
        if 'x' in poly:
            if poly == 'x':
                ans_x += 1
            else:
                ans_x += int(poly.replace('x',''))
        else:
            ans_num += int(poly)
            
    if ans_x:
        answer.append(f"{ans_x}x" if ans_x != 1 else "x")
    if ans_num:
        answer.append(str(ans_num))
    return " + ".join(answer)
