d = [0] * 31

for _ in range(28):
    d[int(input())] = 1
    
for i in range(1,31):
    if d[i] == 0:
        print(i)