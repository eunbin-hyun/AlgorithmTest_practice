import sys

n = int(input())
commands = [sys.stdin.readline().strip() for _ in range(n)]
stack = []

for command in commands:
    if command != '0':
        stack.append(int(command))
    else:
        if stack:
            stack.pop()

print(sum(stack))
