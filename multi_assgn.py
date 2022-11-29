def findExtremeDivisors(n1, n2):
 minVal, maxVal = None, None
 for i in range(2, min(n1, n2) + 1):
    if n1%i == 0 and n2%i == 0:
     if minVal == None or i < minVal:
        minVal = i
     if maxVal == None or i > maxVal:
        maxval =i 
 return (minVal, maxVal)

a=int(input('Enter first number ' ))
b=int(input('Enter second number '))
minDivisor, maxDivisor=findExtremeDivisors(a,b)
print('Minimum divisor: ',minDivisor,'Maximum divisor: ',maxDivisor)
