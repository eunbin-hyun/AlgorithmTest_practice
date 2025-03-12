def solution(my_string):
    string = my_string.split()
    answer = int(string[0])
    
    for i in range(1, len(string), 2):
        operater = string[i]
        number = int(string[i+1])
        
        if operater == "+":
            answer += number
        elif operater == "-":
            answer -= number
    return answer