def solution(date1, date2):
    answer = 0
    y1, m1, d1 = date1
    y2, m2, d2 = date2
    if y1 < y2:
        answer =1
    elif y1 == y2:
        if m1 < m2:
            answer =1
        elif m1 == m2:
            if d1 < d2:
                answer = 1
    return answer