
n = int(input())

k = 2
result = 4

for i in range(n):
    k = 2*k-1
    result = k**2
    
print(result)