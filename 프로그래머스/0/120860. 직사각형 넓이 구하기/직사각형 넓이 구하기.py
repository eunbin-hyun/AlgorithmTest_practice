def solution(dots):
    x_vals = [dot[0] for dot in dots]
    y_vals = [dot[1] for dot in dots]
    return (max(x_vals)-min(x_vals)) * (max(y_vals)-min(y_vals))