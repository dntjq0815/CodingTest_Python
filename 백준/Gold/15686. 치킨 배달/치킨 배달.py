from itertools import combinations

N, M = map(int, input().split())
houses = []
chickens = []
for i in range(N):
    for j, v in enumerate(map(int, input().split())):
        if v == 1:
            houses.append((i, j))
        elif v == 2:
            chickens.append((i, j))


def get_dist(x, y):
    return abs(x[0] - y[0]) + abs(x[1] - y[1])


answer = 2 * N * len(houses)

for combination in combinations(chickens, M):
    total = 0
    for house in houses:
        total += min(get_dist(house, chicken) for chicken in combination)

    answer = min(answer, total)

print(answer)