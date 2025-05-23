def solution(people, limit):
    people.sort(reverse=True)
    cnt = 0
    for i in people:
        if i + people[-1] <= limit:
            people.pop()
        cnt += 1
    return cnt