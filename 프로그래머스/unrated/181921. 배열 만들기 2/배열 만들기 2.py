def solution(l, r):
    answer = []
    for num in range(l, r+1):
        check = True
        for s in str(num):
            if s != '0' and s != '5':
                check = False
                break
        if check == True:
            answer.append(num)

    if not answer:
        return [-1]
    
    return answer