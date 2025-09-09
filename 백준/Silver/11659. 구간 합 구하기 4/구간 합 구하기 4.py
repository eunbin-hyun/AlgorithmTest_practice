import sys
input = sys.stdin.readline

n, m = map(int, input().split())

array = list(map(int, input().split()))
sum_array = [0 for _ in range(n+1)]

for i in range(1,n+1):
    sum_array[i] = array[i-1] + sum_array[i-1] 
    
for _ in range(m):
    i, j = map(int, input().split())
    result = sum_array[j] - sum_array[i-1]
    print(result)
    