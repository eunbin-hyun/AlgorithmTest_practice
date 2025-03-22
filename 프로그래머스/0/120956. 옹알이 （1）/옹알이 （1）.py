def solution(babbling):
    answer = 0
    say =  ["aya", "ye", "woo", "ma"]
    for i in babbling:
        result = 0
        for j in range(4):
            if i.find(say[j]) != -1:
                result += len(say[j])
        if len(i) == result:
            answer += 1
    return answer