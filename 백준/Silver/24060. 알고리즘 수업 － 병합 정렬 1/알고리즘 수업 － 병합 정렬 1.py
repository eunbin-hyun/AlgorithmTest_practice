import sys
input = sys.stdin.readline

N, K  = map(int, input().split())
A = list(map(int, input().split()))
cnt = 0

def merge_sort(A, left, right):
    global cnt
    if left < right:
        center = (left + right) // 2

        merge_sort(A, left, center)
        merge_sort(A, center+1, right)

        p = j = 0       # buff index (실제, 진행)
        i = k = left    # A[] index (실제, 진행)

        # 배열 A 앞부분 buff에 복사
        while i <= center:
            buff[p] = A[i]
            p += 1
            i += 1
        
        # 배열 A 뒷부분과 buff 병합
        while i <= right and j < p:
            if buff[j] <= A[i]:
                A[k] = buff[j]
                j += 1
            else:
                A[k] = A[i]
                i += 1
            k += 1
            cnt += 1
            
            if cnt == K:
                print(A[k-1])
        
        # buff의 나머지원소 배열 A에 복사
        while j < p:
            A[k] = buff[j]
            k += 1
            j += 1
            cnt += 1

            if cnt == K:
                print(A[k-1])
        
        # A배열 남은거 카운트!!
        while i <= right:
            A[k] = A[i]
            i += 1
            k += 1
            cnt += 1

            if cnt == K:
                print(A[k-1])


buff = [None] * N
merge_sort(A, 0, N-1)

if cnt < K:
    print(-1)