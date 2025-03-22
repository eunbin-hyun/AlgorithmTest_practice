def solution(id_pw, db):
    answer = ''
    for i,j in db:
        if id_pw[0] == i and id_pw[1] ==j:
            answer = 'login'
            break
        elif id_pw[0] == i and id_pw[1] != j:
            answer = 'wrong pw'
            break
        else:
            answer = 'fail'
    return answer