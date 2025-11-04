from collections import deque

n, k = map(int, input().split())
belt = list(map(int, input().split()))

front = 0 # 올리는 위치 인덱스
end = n-1 # 내리는 위치 인덱스
cnt = 0 # 수행 단계
zero = 0
robot = deque() #로봇의 인덱스 넣기


while True:
    cnt += 1

    # 1) 전체 컨베이어 돌리기
    front = (front-1)%(2*n)
    end = (end-1)%(2*n)
    # 로봇은 가만히 컨베이어 벨트가 움직임(로봇 움직임처리 됨)
    if robot:
        for _ in range(len(robot)):
            t = robot.popleft()
            # robot이 end와 같으면 아웃
            if t == end:
                continue
            # 2) 로봇 이동가능하면 이동(앞에 로봇이없고 그칸 내구도 1이상)
            if belt[(t+1)%(2*n)] >= 1 and (t+1)%(2*n) not in robot:
                t = (t+1)%(2*n)
                belt[t] -= 1
                if belt[t] == 0:
                    zero +=1
                # robot이 end외 같으면 아웃
                if t == end:
                    continue
            robot.append(t)
    # 3) 내구도 0 아니면 로봇올림
    if belt[front] != 0:
        robot.append(front)
        belt[front] -= 1
        if belt[front] == 0:
            zero += 1

    # 제로 개수 같으면 종료
    if zero >= k:
        break


print(cnt)
