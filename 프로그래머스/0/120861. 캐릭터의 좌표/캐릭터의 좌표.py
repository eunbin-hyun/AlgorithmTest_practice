def solution(keyinput, board):
    answer = [0,0]
    x = (board[0]-1) //2
    y = (board[1]-1) //2
    for i in keyinput:
        if i == "left":
            answer[0] -= 1
        if i == "right":
            answer[0] += 1
        if i == "down":
            answer[1] -= 1
        if i == "up":
            answer[1] += 1
            
        if answer[0] >= x:
            answer[0] = x
        if answer[0] <= -x:
            answer[0] = -x
        if answer[1] >= y:
            answer[1] = y
        if answer[1] <= -y:
            answer[1] = -y
    return answer