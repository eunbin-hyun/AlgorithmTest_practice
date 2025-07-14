N = int(input())
result = 0

for num in range(1,N):
    sum_num = num + sum(int(d) for d in str(num))
    if sum_num == N:
        result = num
        break
    
print(result)