def star(n):
    # --- Base case ---
    if n == 1:
        return ['*']   # n=1이면 그냥 '*' 하나짜리 문자열 리스트 리턴

    # --- Recursive step ---
    arr = star(n//3)   # 더 작은 패턴 생성 (1/3 크기)
    result = []        # 이번 단계에서 만들어질 n x n 패턴 담을 리스트

    # --- 윗부분 ---
    for i in arr:
        result.append(i*3)
        # 작은 패턴 문자열 i를 가로로 3번 반복 → 윗줄 완성

    # --- 가운데 부분 ---wnf
    for i in arr:
        result.append(i + ' '*(n//3) + i)
        # 왼쪽: 작은 패턴 i
        # 가운데: 공백 n//3 개
        # 오른쪽: 작은 패턴 i
        # → 가운데가 뚫린 줄 생성

    # --- 아랫부분 ---
    for i in arr:
        result.append(i*3)
        # 윗부분과 동일: 작은 패턴을 가로 3번 반복

    return result   # 완성된 n x n 패턴 리턴

n = int(input())           # 입력받기
print('\n'.join(star(n)))  # 리스트를 줄바꿈으로 이어서 출력
