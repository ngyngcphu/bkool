# Recursive approach
def lessThan(lst, n):
    if not lst:
        return []
    else:
        smaller_numbers = lessThan(lst[1:], n)
        if lst[0] < n:
            return [lst[0]] + smaller_numbers
        else:
            return smaller_numbers
        
# List comprehension approach
def lessThan(lst, n):
    return [i for i in lst if i < n]

# High-order function approach
def lessThan(lst, n):
    return list(filter(lambda x: x < n, lst))