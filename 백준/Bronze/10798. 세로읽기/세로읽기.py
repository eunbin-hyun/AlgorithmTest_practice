
matrix = [[] for i in range(5)]

max_len = 0
for i in range(5):
    matrix[i] = list(str(input()))
    max_len = max(max_len, len(matrix[i]))

num = 0
for i in range(5):
    if len(matrix[i]) < max_len:
        num = max_len-len(matrix[i])
        for _ in range(num):
            matrix[i].append(' ')
    
for i in range(max_len):
    for j in range(5):
        if matrix[j][i]:
            print(matrix[j][i].replace(" ",""), end='')