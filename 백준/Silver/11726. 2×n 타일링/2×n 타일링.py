MOD = 10007
n = int(input())

squares = [0] * 1001
squares[1] = 1
squares[2] = 2

for i in range(3, 1001):
    squares[i] = (squares[i-1] + squares[i-2]) % MOD

print(squares[n])