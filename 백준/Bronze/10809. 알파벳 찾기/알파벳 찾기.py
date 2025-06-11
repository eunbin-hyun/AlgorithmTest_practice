S = input()
k = [-1]*26

for i in range(len(S)):
    if k[ord(S[i]) -97] == -1:
        k[ord(S[i]) -97] = i
    
for i in k:
    print(i,end=' ')