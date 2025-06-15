k = list(map(int,input().split()))
result = [0]*6

for i in range(len(k)):
    if i == 0 or i ==1:
        result[i] = 1-k[i]
    elif i == 2 or i ==3 or i ==4:
        result[i] = 2-k[i]
    elif i == 5:
        result[i] = 8-k[i]
        
print(" ".join(map(str,result)))