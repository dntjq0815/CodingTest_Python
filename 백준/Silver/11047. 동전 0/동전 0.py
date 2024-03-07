import sys

N, K = map(int, input().split())

coins = [int(sys.stdin.readline()) for _ in range(N)]

count = 0
for coin in coins[::-1]:
    if K // coin > 0:
        count += (K // coin)
        K %= coin

    if K == 0:
        break

print(count)