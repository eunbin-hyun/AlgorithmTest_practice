matrix = [[] for _ in range(9)]

for i in range(9):
    matrix[i] = input().split()

max_num = 0
row = -1
col = -1
for i in range(9):
    for j in range(9):
        max_num = max(max_num, int(matrix[i][j]))
        if max_num == int(matrix[i][j]):
            row, col = i, j
        
print(max_num)
print(row+1, col+1)
