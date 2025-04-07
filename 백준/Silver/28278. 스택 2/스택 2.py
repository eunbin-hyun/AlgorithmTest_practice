import sys
n = int(input())
commands = [sys.stdin.readline().strip() for _ in range(n)]
stack = []

for command in commands:
    if command[0] == '1':
        _ , x = command.split()
        stack.append(x)
    elif command == '2':
        if stack:
            print(stack.pop())
        else:
            print(-1)  
    elif command == '3':
        print(len(stack))
    elif command == '4':
        if stack:
            print(0)
        else:
            print(1) 
    elif command == '5':
        if stack:
            print(stack[-1])
        else:
            print(-1) 