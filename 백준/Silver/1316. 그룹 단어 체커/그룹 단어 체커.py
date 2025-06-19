n = int(input())
count = 0

for i in range(n):
    alp = [0]*30
    k =input()
    s = k[0]
    alp[ord(s)-ord('a')] += 1 
    for j in range(1,len(k)):
        if s == k[j]:
            s = k[j] 
            continue
        s = k[j]
        alp[ord(s)-ord('a')] += 1 
    if max(alp) == 1:
        count += 1 
    
print(count)