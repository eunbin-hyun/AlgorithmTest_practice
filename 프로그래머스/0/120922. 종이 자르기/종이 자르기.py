def solution(M, N):
    if M == 1 and N ==1:
        return 0
    answer = (M-1) + (M*(N-1))
    return answer