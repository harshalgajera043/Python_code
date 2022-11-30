def arithmetic(a,b):
    addition=a+b
    substraction=a-b
    multiplication=a*b
    division=a/b
    return(addition, substraction, multiplication, division)
a=int(input('Enter first number'))
b=int(input('Enter second number'))
(add,sub,mul,div)=arithmetic(a,b)
print('Addition :',add,'Substraction :',sub,'Multiplication :',mul,'Division :',div)
    
