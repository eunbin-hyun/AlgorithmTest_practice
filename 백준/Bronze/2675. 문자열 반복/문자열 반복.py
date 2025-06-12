T = int(input())
result = ''

for i in range(T):
    R,S = map(str, input().split())
    for j in S:
        result += j*int(R)
    print(result)
    result = ''