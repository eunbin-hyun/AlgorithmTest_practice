def solution(chicken):
    answer = 0
    k = chicken
    a=0
    b=0
    while k //10 > 0:
        a = k//10
        b = k%10
        answer += a
        k = a+b
    return answer