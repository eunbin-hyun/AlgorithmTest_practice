S = input().strip()
p = input().strip()

stack = []

for s in S:
    stack.append(s)
    if len(stack) >= len(p) and stack[-1] == p[-1]:
        tmp = []
        for _ in range(len(p)):
            k = stack.pop()
            tmp.append(k)
        if tmp != list(p[::-1]):
            for k in tmp[::-1]:
                stack.append(k)

if stack:
    for s in stack:
        print(s, end="")
else:
    print("FRULA")
            
