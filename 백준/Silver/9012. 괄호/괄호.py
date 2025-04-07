import sys

n = int(input())
commands = [sys.stdin.readline().strip() for _ in range(n)]

for command in commands:
    stack = []
    for i in command:
        if i == '(':
            stack.append(i)
        else:
            if not stack:
                print("NO")
                break
            stack.pop()
    else:  # for-else: break 없이 끝까지 돌았으면 여기 실행
        if stack:
            print("NO")
        else:
            print("YES")