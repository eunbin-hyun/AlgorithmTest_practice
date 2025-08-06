from collections import deque 
import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    A, B = map(int, input().split())
    A_list = deque()
    k_list = deque()
    for i in range(1,A+1):
        if A % i == 0:
            A_list.append(i)
    for i in range(1, B+1):
        if B % i == 0 and i in A_list:
            k_list.append(i)
    
    print(A*B//max(k_list))
 