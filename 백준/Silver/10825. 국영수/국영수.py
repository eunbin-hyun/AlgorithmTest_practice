n = int(input())

array = []
for _ in range(n):
    name, kor, eng, math = input().split()
    array.append((name, int(kor), int(eng), int(math)))
    
array.sort(key = lambda stu: (-stu[1], stu[2], -stu[3], stu[0]))
# 여려개 정렬대상일 때 튜플형태로 묶어서 표현가능

for stu in array:
    print(stu[0])