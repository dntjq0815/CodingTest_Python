MOD = 1000000000

cache = [[0] * 10 for _ in range(101)]
for j in range(1, 10):
    cache[1][j] = 1

for i in range(2, 101):
    for j in range(10):
        if j > 0:
            cache[i][j] += cache[i - 1][j - 1]
            cache[i][j] %= MOD
        if j < 9:
            cache[i][j] += cache[i - 1][j + 1]
            cache[i][j] %= MOD

count = 0
N = int(input())
for j in range(10):
    count += cache[N][j]
    count %= MOD

print(count)