N, L = map(int, input().split())
coord = [False] * 1001

for i in map(int, input().split()):
    coord[i] = True

x = 0
count = 0
while x < 1001:
    if coord[x]:
        count += 1
        x += L
    else:
        x += 1

print(count)