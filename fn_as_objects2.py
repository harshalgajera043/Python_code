def factorial(n):
    """assumes that n is an int > 0
    returns n!"""
    if n == 1:
        return n 
    else:
        return n*factorial(n-1)
def square(n):
    return n**2


L = [1, 3, 5]
print('list with factorial = ',list(map(factorial, L)))
print('list with square=', list(map(square, L)))                