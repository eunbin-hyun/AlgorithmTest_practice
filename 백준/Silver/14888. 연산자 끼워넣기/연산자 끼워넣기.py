n = int(input())
array = list(map(int, input().split()))
k = list(map(int, input().split()))

maxval = -1e10
minval = 1e10

def dfs(num, i, add, sub, mul, div):
    global maxval, minval

    # 모든 숫자를 다 썼다면 i==n -> 리프노드 도달
    if i == n:
        maxval = max(maxval, num)
        minval = min(minval, num)
        return
    
    # 아직 사용할 숫자가 남았다면, 남은 연산자 하나씩 사용해 재귀호출
    else:
        if add:
            dfs(num+array[i], i+1, add-1, sub, mul, div)
        if sub:
            dfs(num-array[i], i+1, add, sub-1, mul, div)
        if mul:
            dfs(num*array[i], i+1, add, sub, mul-1, div)
        if div:
            dfs(int(num/array[i]), i+1, add, sub, mul, div-1)
        
dfs(array[0], 1, k[0], k[1], k[2], k[3])
print(maxval)
print(minval)

