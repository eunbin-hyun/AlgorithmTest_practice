m,n = map(int, input().split())
array = [True for i in range(n+1)]
array[1] = 0

    
for i in range(2, int(n**(0.5)) +1):
    if array[i] == True: # i가 소수인 경우
        j = 2
        while i * j <= n:
            array[i*j] = False
            j += 1 
    
for i in range(m, n+1):
    if array[i]:
        print(i)