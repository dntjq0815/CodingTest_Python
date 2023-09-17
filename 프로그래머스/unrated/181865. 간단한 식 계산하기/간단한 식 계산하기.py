def solution(binomial):
    
    a, op, b = binomial.split()
    
    a = int(a)
    b = int(b)
    
    return calc(a, op, b)


def calc(a, op, b):
    if op == '+':
        return a + b
    
    elif op == '-':
        return a - b
    
    else:
        return a * b