def solution(s):
    stack = []
    for i in s:
        if i == '(':
            stack.append(i)
        else:
            if stack == []:
                return False
                break
            else:
                stack.pop()

    if stack != []:
        return False

    return True