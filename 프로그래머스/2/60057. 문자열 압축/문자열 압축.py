def solution(s):
    answer = len(s)
    for  step in range(1, len(s)//2 + 1):
        compressed = ""
        prev = s[0:step]
        count = 1
        # step크기만큼 증가시키며 이전 문자열 과 비교
        for j in range(step, len(s), step):
            # 이전 상태와 동일하다면 압축 count +1
            if prev == s[j:j + step]:
                count += 1
            # 압축 못한경우
            else:
                compressed += str(count) + prev if count >= 2 else prev
                prev = s[j:j + step]  # 다시 상태 초기화
                count = 1
        # 남아 있는 문자열에 대해서 처리
        compressed += str(count) + prev if count >= 2 else prev
        # 만들어지는 압축 문자열이 가장 짧은 것이 정답
        answer = min(answer, len(compressed))
    return answer