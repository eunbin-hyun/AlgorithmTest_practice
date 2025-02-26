def solution(n, lost, reserve):
    # 정렬
    lost.sort()
    reserve.sort()
    
    # lost, reserve에 공통으로 있는 요소 제거
    for i in reserve[:]:
        if i in lost:
            reserve.remove(i)
            lost.remove(i)
    
    for i in reserve:
        if i-1 in lost:
            lost.remove(i-1)
        elif i+1 in lost:
            lost.remove(i+1)
    answer = n - len(lost)
    return answer