def solution(l, r):
    answer = []
    
    for i in range(l, r+1):
        check = True
        ch = str(i)
        
        for j in ch:
            if j != "0" and j != "5":
                check = False
                break
            
        if check == True:
            answer.append(i)
        
    if not answer:
        return [-1]
        
    return answer