def solution(numbers):
    answer = ''
    ans = ''
    num = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for i in numbers:
        ans += i
        if ans in num:
            answer += str(num.index(ans))
            ans = ''
    return int(answer)