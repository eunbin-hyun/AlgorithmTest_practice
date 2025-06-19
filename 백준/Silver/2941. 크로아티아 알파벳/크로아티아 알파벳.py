s= input()
alp= ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

n= 0
count = 0
i=1

while n < len(s):
    if n+i <= len(s):
        if s[n:n+i] in alp:
            count += 1 
            n = n+i 
            i = 1 
            continue
        if i >= 3:
            n += 1
            i = 1 
            count += 1 
            continue
        i += 1
    else:
        count += (len(s)- n)
        n = len(s)
        
print(count)
    