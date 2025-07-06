x =[0]*4
y=[0]*4
for i in range(3):
    x[i],y[i] = map(int, input().split())
    
for j in range(3):
    if x.count(x[j]) == 1:
        x[3] = x[j]
    if y.count(y[j]) == 1:
        y[3] = y[j]
        
print(x[3], y[3])