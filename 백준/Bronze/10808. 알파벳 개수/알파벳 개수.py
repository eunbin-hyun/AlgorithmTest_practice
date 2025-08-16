S = input()

alp = [0 for i in range(ord('z')-ord('a')+1)]

for s in S:
    alp[ord(s)-ord('a')] += 1

print(*alp)