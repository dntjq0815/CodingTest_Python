from collections import deque

N, M = map(int, input().split())

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

maze = [[] * 4 for _ in range(N)]
for i in range(N):
    rows = input()
    for row in rows:
        maze[i].append(int(row))


def bfs(x, y):
    dq = deque()
    dq.append((x, y))
    while dq:
        x, y = dq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue
            if maze[nx][ny] == 0:
                continue
            if maze[nx][ny] == 1:
                maze[nx][ny] = maze[x][y] + 1
                dq.append((nx, ny))

    return maze[N-1][M-1]

print(bfs(0, 0))