from collections import deque 
wheel = [[], [], [], []]

for i in list(input().strip()):
    wheel[0].append(int(i))
for i in list(input().strip()):
    wheel[1].append(int(i))
for i in list(input().strip()):
    wheel[2].append(int(i))
for i in list(input().strip()):
    wheel[3].append(int(i))

clock3 = [2,2,2,2]
clock9 = [6,6,6,6]
queue = deque()

n = int(input())
for _ in range(n):
    change = [0, 0, 0, 0]
    num, dic = map(int, input().split())
    queue.append([num-1, dic])
    while queue:
        num, dic = queue.pop()
        change[num] = dic
        # pop된 톱니바퀴의 왼쪽 비교
        if num != 0:
            if wheel[num-1][clock3[num-1]] != wheel[num][clock9[num]] and change[num-1] == 0:
                if dic == 1:
                    queue.append([num-1, -1])
                else:
                    queue.append([num-1, 1])
        # pop된 톱니바퀴의 오른쪽 비교
        if num != 3:
            if wheel[num][clock3[num]] != wheel[num+1][clock9[num+1]] and change[num+1] == 0:
                if dic == 1:
                    queue.append([num+1, -1])
                else:
                    queue.append([num+1, 1])

    # 변화 업데이트
    for i in range(4):
        if change[i] == -1:
            clock3[i] = (clock3[i]+1)%8
            clock9[i] = (clock9[i]+1)%8
        elif change[i] == 1:
            if clock3[i]-1 == -1:
                clock3[i] = 8
            clock3[i] = (clock3[i]-1)%8
            clock9[i] = (clock9[i]-1)%8

clock12 = []
for i in range(4):
    k = (clock3[i]-2)%8
    clock12.append(wheel[i][k])

result = clock12[0]*1 + clock12[1]*2 + clock12[2]*4 + clock12[3]*8

print(result)