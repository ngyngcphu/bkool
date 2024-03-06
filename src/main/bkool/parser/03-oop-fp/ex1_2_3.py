# Recursive approach
def lstSquare(n):
    if n == 0:
        return []
    else:
        squares = lstSquare(n - 1)
        squares.append(n ** 2)
        return squares
    
# List comprehension approach
def lstSquare(n):
    return [i * i for i in range (1, n + 1)]

# High-order function approach
def lstSquare(n):
    return list(map(lambda x: x * x, range(1, n + 1)))