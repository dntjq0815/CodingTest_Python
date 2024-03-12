from bisect import bisect_left, bisect_right

N = int(input())
cards = sorted(map(int, input().split()))
M = int(input())
find_cards = list(map(int, input().split()))

answer = []
for card in find_cards:
    l = bisect_left(cards, card)
    r = bisect_right(cards, card)

    if r - l > 0:
        answer.append(1)
    else:
        answer.append(0)

print(*answer)