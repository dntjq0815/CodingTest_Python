import sys

N, P = map(int, input().split())
codes = [[] for _ in range(7)]

count = 0
for _ in range(N):
    n, p = map(int, sys.stdin.readline().split())

    while codes[n] and codes[n][-1] > p:
        codes[n].pop()
        count += 1

    if codes[n] and codes[n][-1] == p:
        continue

    codes[n].append(p)
    count += 1

print(count)