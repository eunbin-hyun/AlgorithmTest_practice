s= input()
alp= ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for a in alp:
    s = s.replace(a,'*')
        
print(len(s))
    