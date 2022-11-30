# Bisectiob search with function to approximate root
#Factorial with  function
def factorial(n):
    """Assumption: Assumes n as an int, n>0
Guarantees: Returns int num as factorial of n, num >0 """
    num = 1
    while n >=1:
        num = num * n
        n = n - 1
    return num

print('Factorial of 5',factorial(5))
print('The docstring of the function root: ',factorial.__doc__) #Also, we can access the 
