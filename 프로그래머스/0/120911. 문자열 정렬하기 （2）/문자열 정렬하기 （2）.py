def solution(my_string):
    ans = list(my_string.lower())
    ans.sort()
    return "".join(ans)