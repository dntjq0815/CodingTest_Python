book_dict = dict()
for _ in range(int(input())):
    book = input()
    if book not in book_dict:
        book_dict[book] = 0
    book_dict[book] += 1

b_max = max(book_dict.values())
max_list = []
for k, v in book_dict.items():
    if b_max == v:
        max_list.append(k)

print(sorted(max_list)[0])