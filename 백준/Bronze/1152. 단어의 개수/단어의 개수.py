S = input()
K = []
K = S.split(" ")
result = 0

for i in K:
    if i != '':
        result += 1
        
print(result)