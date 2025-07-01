n = int(input())
count = 0
result = 1

while result < n:
        count += 1
        result += 6*count
    
print(count+1)