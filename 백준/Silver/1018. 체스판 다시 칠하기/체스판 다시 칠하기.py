N, M = map(int, input().split())
board = [input() for _ in range(N)]
answer = 64


def fill(x, y, bw):
    global answer
    count = 0
    for i in range(8):
        for j in range(8):
            if (i+j) % 2 == 0:
                if board[x + i][y + j] != bw:
                    count += 1
            else:
                if board[x + i][y + j] == bw:
                    count += 1

    answer = min(answer, count)


for i in range(N - 7):
    for j in range(M - 7):
        fill(i, j, 'B')
        fill(i, j, 'W')

print(answer)