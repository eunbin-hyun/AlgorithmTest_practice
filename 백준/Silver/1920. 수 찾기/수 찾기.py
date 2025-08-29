import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))

A.sort()

for b in B:
    start, end = 0, n-1
    is_true = False
    while start <= end:
        mid = (start+end)//2
        if A[mid] == b:
            print(1)
            is_true = True
            break
        elif A[mid] > b:
            end = mid -1
        elif A[mid] < b:
            start = mid +1 
    if is_true == False:
        print(0)
    
    