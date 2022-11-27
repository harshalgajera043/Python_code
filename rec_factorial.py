def factorial(n):
    """Assumes that n is an int > 0
    Returns n!"""
    if n == 0 or n==1:
        return 1
    else:
        return n*factorial(n - 1)

n=int(input('Enter a number of which factorial is to be calculated: '))
ans=factorial(n)
print('factorial of',n,'is',ans)
        
