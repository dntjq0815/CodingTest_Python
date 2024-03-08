import sys
sys.setrecursionlimit(10 ** 6)

N, M = map(int, input().split())

adj = [[0] * N for _ in range(N)]
for _ in range(M):
    u, v = map(lambda x: x-1, map(int, sys.stdin.readline().split()))
    adj[u][v] = adj[v][u] = 1

visited = [False] * N
def dfs(now):
    for nxt in range(N):
        if adj[now][nxt] and not visited[nxt]:
            visited[nxt] = True
            dfs(nxt)


count = 0
for i in range(N):
    if not visited[i]:
        count += 1
        visited[i] = True
        dfs(i)

print(count)