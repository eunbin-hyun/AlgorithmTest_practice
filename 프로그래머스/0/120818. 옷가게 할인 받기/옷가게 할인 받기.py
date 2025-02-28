def solution(price):
    answer = 0
    
    if price < 100000:
        answer = price
    elif price >= 100000 and price < 300000:
        answer = price * 0.95
    elif price >= 300000 and price < 500000:
        answer = price * 0.9
    elif price >= 500000:
        answer = price * 0.8
    return int(answer)