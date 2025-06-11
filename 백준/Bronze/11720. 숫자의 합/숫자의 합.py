n = int(input())
s = input()

result = int(s[0])
for i in range(1,n):
    result += int(s[i])
    
print(result)
