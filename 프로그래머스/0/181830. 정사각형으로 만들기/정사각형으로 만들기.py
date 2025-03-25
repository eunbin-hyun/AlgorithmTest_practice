def solution(arr):
    row = len(arr)
    col = len(arr[0])
    if row > col:
        for i in arr:
            for j in range(row - col):
                i.append(0)
    elif row < col:
        for j in range(col - row):
            arr.append([0]*col)
    return arr