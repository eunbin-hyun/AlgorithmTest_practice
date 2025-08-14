from collections import deque

n = int(input())
moves = list(map(int, input().split()))
bul = deque((i+1, moves[i]) for i in range(n))

k = bul.popleft()
print(k[0], end=" ")

for _ in range(n-1):
    if k[1] > 0:
        for _ in range(k[1]-1):
            tmp= bul.popleft()
            bul.append(tmp)
    else:
        for _ in range(-k[1]):
            tmp = bul.pop()
            bul.appendleft(tmp)
    k=bul.popleft()
    print(k[0], end=" ")
    
