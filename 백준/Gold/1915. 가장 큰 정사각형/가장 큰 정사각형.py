n, m = map(int, input().split())
arr = [input() for _ in range(n)]
dp = [[0] * m for _ in range(n)]

for j in range(m):
    if arr[0][j] == '1':
        dp[0][j] = 1

for i in range(1, n):
    if arr[i][0] == '1':
        dp[i][0] = 1

    for j in range(1, m):
        if arr[i][j] == '1':
            dp[i][j] = min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1]) + 1

answer = 0
for i in range(n):
    for j in range(m):
        answer = max(answer, dp[i][j])

print(answer ** 2)