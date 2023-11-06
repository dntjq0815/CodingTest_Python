def solution(common):
    answer = 0
    for i in range(len(common) - 2):
        if (common[i] - common[i+1]) == (common[i+1] - common[i+2]):
            return common[-1] + (common[i+1] - common[i])
        
        elif (common[i] / common[i+1]) == (common[i+1] / common[i+2]):
            return common[-1] * (common[i+1] / common[i])