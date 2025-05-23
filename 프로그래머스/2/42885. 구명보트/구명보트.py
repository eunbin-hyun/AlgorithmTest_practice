def solution(people, limit):
    people.sort()
    a = 0
    b = len(people) -1
    count = 0
    
    while a <= b:
        if people[b] + people[a] <= limit:
            a += 1
        b -= 1
        count += 1
        
    return count