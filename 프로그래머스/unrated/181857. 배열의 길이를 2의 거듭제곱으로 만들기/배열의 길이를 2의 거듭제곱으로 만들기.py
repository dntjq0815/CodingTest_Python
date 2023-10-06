def solution(arr):
    cnt = 0
    length = len(arr)
    while length > 1:
        length /= 2
        cnt += 1
        
    return arr + [0] * (2 ** cnt - len(arr))