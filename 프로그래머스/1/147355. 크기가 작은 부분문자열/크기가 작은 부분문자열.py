def solution(t, p):
    answer = 0
    len_p = len(p)
    i = 0
    while i+len_p <= len(t):
        if t[i:i + len_p] <= p:
            answer += 1
        i += 1
    
    return answer