import sys
input = sys.stdin.readline

T = int(input())
nList = []

for _ in range(T):
    nList.append(int(input()))
    
prime = [0 for _ in range(max(nList)+1)]  
    
    
for i in range(2, max(nList)+1):   
    isprime = True
    for j in range(2, int(i**0.5)+2):
        if i%j ==0:
            prime[i]= False
            isprime =False
            break
    if isprime == True:
        prime[i] = True
prime[2] = True

for n in nList:
    cnt = 0
    for i in range(2, n//2 +1):
        if prime[i] == True and prime[n-i] == True:
            cnt += 1
    print(cnt)
 