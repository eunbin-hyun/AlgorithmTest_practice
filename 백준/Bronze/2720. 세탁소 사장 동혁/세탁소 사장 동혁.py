t = int(input())
c = []

for _ in range(t):
    c.append(int(input()))
    
for i in c:
    print(i//25, end=' ')
    print((i%25)//10, end=' ')
    print(((i%25)%10)//5, end=' ')
    print((((i%25)%10)%5)//1)