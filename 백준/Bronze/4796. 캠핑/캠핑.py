count = 1
while True:
    L, P, V = map(int, input().split())

    if L == 0:
        break

    print(f'Case {count}: {V // P * L + min(L, V % P)}')
    count += 1