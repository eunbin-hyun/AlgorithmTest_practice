h, m = map(int, input().split())
c = int(input())

m += c 
h += (m//60)
m %= 60
h %= 24
print(h,m)