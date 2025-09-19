def solution(queue1, queue2):
    cnt = 0
    list = queue1+queue2
    k = len(list)
    front = 0
    rear = len(queue1)
    sum1 = sum(list[front:rear])
    
    if sum(list)%2 !=0:
        return -1
    total = sum(list)//2
    limit = k*2
    
    while cnt <= limit:
        if sum1 == total:
            return cnt
        elif sum1 > total:
            sum1 -= list[front]
            front = (front + 1)%k
        else:
            sum1 += list[rear]
            rear = (rear + 1)%k
        cnt += 1
        
    return -1

    