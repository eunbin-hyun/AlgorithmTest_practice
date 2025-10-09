n = int(input())
array = list(map(int, input().split()))
k = list(map(int, input().split()))

stack = []
max_value = -1000000001
min_value = 1000000001

def back():
    if len(stack) == n-1:
        result = array[0]
        for num in range(n-1):
            if stack[num] == 0:
                result += array[num+1]
            elif stack[num] == 1:
                result -= array[num+1]
            elif stack[num] == 2:
                result *= array[num+1]
            elif stack[num] == 3:
                result = int(result/array[num+1])

        global max_value
        global min_value
        if result >= max_value:
            max_value = result
        if result <= min_value:
            min_value = result
        return

    for i in range(4):
        if k[i] >0 :
            k[i] -= 1
            stack.append(i)
            back()
            stack.pop()
            k[i] += 1

back()
print(max_value)
print(min_value)

