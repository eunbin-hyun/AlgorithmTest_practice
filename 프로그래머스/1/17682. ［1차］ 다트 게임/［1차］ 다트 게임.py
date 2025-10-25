def solution(dartResult):
    answer = 0
    ans = [0]*3
    temp =""
    i = 0
    for star in dartResult:
        if star.isdigit():
            temp += star
        elif star.isalpha():
            if star == 'S':
                ans[i] = int(temp)**1
            elif star == 'D':
                ans[i] = int(temp)**2
            elif star == 'T':
                ans[i] = int(temp)**3
            temp = ""
            i += 1
            
        else:   
            if star == '*':
                ans[i-1] *= 2
                if (i-1) != 0:
                    ans[i-2] *= 2
            elif star == '#':
                ans[i-1] *= -1

    answer = sum(ans)        
    return answer