def solution(strArr):
    answer = []
    tmp = [len(str) for str in strArr]
    
    for str in set(tmp):
        answer.append(tmp.count(str))
        
    return max(answer)