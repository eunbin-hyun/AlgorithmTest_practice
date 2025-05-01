array = [int(input()) for _ in range(9)]

array = list(enumerate(array))
    
array.sort(reverse =True, key = lambda x: x[1])

print(array[0][1])
print(int(array[0][0])+1)