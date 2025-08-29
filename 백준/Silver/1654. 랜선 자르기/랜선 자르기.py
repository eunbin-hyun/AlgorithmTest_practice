import sys
input = sys.stdin.readline

k, n = map(int, input().split())
lan = []

for _ in range(k):
    lan.append(int(input()))
    
start = 1
end = max(lan)

result = 0
while start <= end:
    cnt = 0
    mid = (start + end) //2
    for x in lan:
        cnt += x // mid
    if cnt < n:
        end = mid -1
    else:
        result = mid
        start = mid + 1
        
print(result)