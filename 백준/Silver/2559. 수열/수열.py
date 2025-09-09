import sys
input = sys.stdin.readline

n, k = map(int, input().split())

array = list(map(int, input().split()))
sum_array = [0 for _ in range(n-k+1)]
sum_array[0] = sum(array[:k])

for i in range(1,n-k+1):
    sum_array[i] = sum_array[i-1] - array[i-1] + array[i+k-1]

print(max(sum_array))