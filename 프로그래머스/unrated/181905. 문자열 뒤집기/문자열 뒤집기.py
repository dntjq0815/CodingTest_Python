def solution(my_string, s, e):
    answer = ''
    for i in range(e, s-1, -1):
        answer += my_string[i]
        
    return my_string[:s] + answer + my_string[e+1:]