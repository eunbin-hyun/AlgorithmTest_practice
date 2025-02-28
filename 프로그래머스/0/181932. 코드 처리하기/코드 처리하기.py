def solution(code):
    
    ret = ''
    mode = False
    
    for idx,i in enumerate(code):
        
        if i == "1":
            mode = not mode
            continue
        
        if not mode and idx % 2 == 0:
            ret +=i
        
        elif mode and idx % 2 == 1:
            ret +=i
        
    if ret == '':
        return "EMPTY"
        
    return ret