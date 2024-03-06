from itertools import permutations

little_list = []
for _ in range(9):
    little_list.append(int(input()))


for little in permutations(little_list, 7):
    if sum(little) == 100:
        for i in sorted(list(little)):
            print(i)
        break