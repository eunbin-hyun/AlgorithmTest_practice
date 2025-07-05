M = int(input())
N = int(input())
result = [-1]*(N+1)
num_list=[]

for i in range(M,N+1):
    cnt = 0
    result[i] = 1
    for j in range(2,i):
        if i%j == 0:
            cnt += 1
            if cnt > 0:
                result[i] = -1
                break 
result[1]= -1
for i in range(len(result)):
    if result[i]==1:
        num_list.append(i)

if sum(num_list) != 0:
    print(sum(num_list))
    print(min(num_list))
else:
    print(-1)