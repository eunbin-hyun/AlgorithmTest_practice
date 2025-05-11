k = []

while True:
    a,b = map(int, input().split())
    if a==0 and b==0:
        break
    k.append((a,b))
    
for i in range(len(k)):
    print(sum(k[i]))