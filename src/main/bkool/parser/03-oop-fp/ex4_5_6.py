# Recursive approach
def dist(lst, n):
    if not lst:
        return []
    else:
        pair = (lst[0], n)
        return [pair] + dist(lst[1:], n)
    
# List comprehension approach
def dist(lst, n):
    return [(i, n) for i in lst]

# High-order function approach
def dist(lst, n):
    return list(map(lambda x: (x, n), lst))