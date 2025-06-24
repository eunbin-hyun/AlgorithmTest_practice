n, b = input().split()
result = 0 
b = int(b)

for i in range(len(n)):
    if '0' <= n[i] <= '9':
        num = int(n[i])
    else:
        num = ord(n[i])-ord('A')+10
    result += (b**(len(n)-i-1))*num
    
print(result)