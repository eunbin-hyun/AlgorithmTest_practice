import sys

while True:
    line = sys.stdin.readline()
    if line == ".\n":
        break

    answer = True
    stack = []

    for word in line:
        if word == "(" or word == "[":
            stack.append(word)
        elif word ==")":
            if not stack:
                answer = False
                break
            k = stack.pop()
            if k != "(":
                answer = False
                break
        elif word =="]":
            if not stack:
                answer = False
                break
            k = stack.pop()
            if k != "[":
                answer = False
                break

    if stack or answer == False:
        print("no")
    else:
        print("yes")

