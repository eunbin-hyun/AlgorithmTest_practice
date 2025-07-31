n = int(input())
n_list = list(map(int, input().split()))

result = []
stack = []
i = 0

while True:
    if i == len(n_list):
        break

    if n_list[i] == len(result)+1:
        result.append(n_list[i])
    else:
        stack.append(n_list[i])
    i += 1

    if stack:
        for _ in range(len(stack)):
            if stack[-1] == len(result)+1:
                k = stack.pop()
                result.append(k)


if len(result) == len(n_list):
    print("Nice")
else:
    print("Sad")
        