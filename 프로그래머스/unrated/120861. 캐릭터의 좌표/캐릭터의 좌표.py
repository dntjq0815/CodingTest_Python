def solution(keyinput, board):
    answer = [0,0]
    x_max = board[0] // 2
    y_max = board[1] // 2
    for dir in keyinput:
        if dir == 'up' and answer[1]+1 <= y_max:
            answer[1] += 1
        elif dir == 'down' and answer[1]-1 >= -(y_max):
            answer[1] -= 1
        elif dir == 'left' and answer[0]-1 >= -(x_max):
            answer[0] -= 1
        elif dir == 'right' and answer[0]+1 <= x_max:
            answer[0] += 1
        
    return answer