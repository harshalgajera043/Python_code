def fib(n):
    """Assumes n an int >=0
    Returns Fibonacci of n"""
    if n == 0 or n == 1: #two base cases
        return n
    else:
        return fib(n-1) + fib(n-2) # two recursive call
n=int(input('Enter a number for Fibonacci: '))
for i in range(n+1):
    print('fib of', i, '=',fib(i))
    
    
