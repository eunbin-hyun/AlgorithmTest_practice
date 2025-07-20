import sys
input = sys.stdin.readline

n = int(input())
people = []

for _ in range(n):
    age, name = input().split()
    people.append([int(age), name])

people.sort(key=lambda x: x[0])

for age, name in people:
    print(age, name)