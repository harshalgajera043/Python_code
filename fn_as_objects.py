import math
def applyToEach(L,f):
    for i in range(len(L)):
        L[i] = f(L[i])
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n*factorial(n-1)

L = [1, -2 ,3.33]
print("L=",L)
print("Apply abs to each element of L", L)
applyToEach(L,abs)
print('L =',L)
print('apply int to each element of L',L)
applyToEach(L, int) 
print('L =',L)
print('apply factorial to each element of L',L)
applyToEach(L, factorial)
print('L =',L)
