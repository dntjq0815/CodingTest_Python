def solution(id_pw, db):
    for data in db:
        if id_pw in db:
            return 'login'
        
        elif id_pw[0] == data[0] and id_pw[1] != data[1]:
            return 'wrong pw'
        
    else:
        return 'fail'