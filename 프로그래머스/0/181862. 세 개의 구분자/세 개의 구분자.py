def solution(myStr):
    answer = myStr.replace('a', ' ').replace('b', ' ').replace('c', ' ')
    ans = answer.split()
    if ans == []:
        ans = ["EMPTY"]
    return ans