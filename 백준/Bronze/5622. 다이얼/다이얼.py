word = input()
result = 0
dial = ['1', 'ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ', '0']

for i in range(len(word)):
    for j in dial:
        if word[i] in j:
            result += (dial.index(j)+2)
print(result)