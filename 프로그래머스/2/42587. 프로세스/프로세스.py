def solution(priorities, location):
    idx = [i for i in range(len(priorities))]
    answer = []

    while priorities:
        if priorities[0] == max(priorities):
            answer.append(idx.pop(0))
            priorities.pop(0)
        else:
            priorities.append(priorities.pop(0))
            idx.append(idx.pop(0))
            print(idx)

    return answer.index(location) + 1