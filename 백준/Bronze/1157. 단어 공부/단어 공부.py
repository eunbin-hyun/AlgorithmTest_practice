s = input()
s = s.upper()
k = [0]*30

for i in s:
    k[ord(i)-ord('A')] += 1 

num = k.count(max(k))
result = k.index(max(k))

if num != 1:
    print("?")
else:
    print(chr(result+ord('A')))