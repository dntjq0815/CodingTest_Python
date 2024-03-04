from collections import deque

def solution(maps):
    answer = 0
    
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    
    n, m = len(maps), len(maps[0])
    def bfs(x, y):
        queue = deque()
        queue.append((x, y))
        
        while queue:
            x, y = queue.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                if nx < 0 or ny < 0 or nx >= n or ny >= m:
                    continue
                    
                if maps[nx][ny] == 0:
                    continue
                    
                if maps[nx][ny] == 1:
                    queue.append((nx, ny))
                    maps[nx][ny] = maps[x][y] + 1
                    
        
    bfs(0,0)
    answer = maps[n-1][m-1]
    
    if answer == 1:
        return -1
                    
    return answer