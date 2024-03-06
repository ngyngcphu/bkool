# Recursive approach
from functools import reduce


def flatten(lst):
    if not lst:
        return []
    else:
        if isinstance(lst[0], list):
            return flatten(lst[0]) + flatten(lst[1:])
        else:
            return [lst[0]] + flatten(lst[1:])
        
# List comprehension approach
def flatten(lst):
    return [j for i in lst for j in i]

# High-order function approach
def flatten(lst):
    return reduce(lambda acc, cur: acc + cur, lst, [])