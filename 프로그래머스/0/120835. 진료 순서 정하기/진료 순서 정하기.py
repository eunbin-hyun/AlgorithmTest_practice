def solution(emergency):
    answer1 = []
    answer2 = []
    
    answer2 = sorted(emergency, reverse = True)
    
    for i in emergency:
        answer1.append(answer2.index(i)+1)
    return answer1