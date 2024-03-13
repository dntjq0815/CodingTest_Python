import sys
sys.setrecursionlimit(10**6)

N, K = map(int, input().split())

cache = [[0] * 1001 for _ in range(1001)]
def bino(n, k):
    if cache[n][k]:
        return cache[n][k]
    if k == 0 or n == k:
        cache[n][k] = 1
    else:
        cache[n][k] = bino(n-1, k-1) + bino(n-1, k)

    return cache[n][k]


print(bino(N, K) % 10007)