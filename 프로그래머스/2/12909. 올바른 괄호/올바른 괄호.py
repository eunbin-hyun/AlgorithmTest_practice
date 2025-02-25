def solution(s):
    stack = []
    stack.append(s[0])
    
    if stack[0] == ')':
        return False
    else:
        for i in s[1:]:
            if stack and stack[-1] == '(' and i == ')':
                stack.pop()
            else:
                stack.append(i)
        if len(stack) ==0:
            return True
        else:
            return False
