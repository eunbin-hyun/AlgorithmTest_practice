def solution(A, B):
    if A==B:
        return 0
    B *= 2
    if A in B:
        return B.find(A)
    return -1