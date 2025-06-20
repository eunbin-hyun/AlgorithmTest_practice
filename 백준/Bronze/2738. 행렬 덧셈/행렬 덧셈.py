n, m = map(int, input().split())
A = []
B = []

for _ in range(n):
    matrix = input().split()
    A.append(matrix)

for _ in range(n):
    matrix2 = input().split()
    B.append(matrix2)
    

for i in range(n):
    for j in range(m):
        print(int(A[i][j])+int(B[i][j]), end=" ")
    print()