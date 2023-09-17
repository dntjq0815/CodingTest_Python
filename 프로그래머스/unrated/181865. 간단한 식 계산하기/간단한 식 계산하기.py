def solution(binomial):
    
    a = int(binomial.split(' ')[0])
    op = binomial.split(' ')[1]
    b = int(binomial.split(' ')[2])
    
    return calc(a, op, b)


def calc(a, op, b):
    if op == '+':
        return a + b
    
    elif op == '-':
        return a - b
    
    else:
        return a * b