def solution(arr, queries):
    answer = []
    for s, e, k in queries:
        filtered_e = [x for x in arr[s:e+1] if x > k]
        
        if filtered_e:
            answer.append(min(filtered_e))
        else:
            answer.append(-1)
        
    return answer