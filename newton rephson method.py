n = float(input("enter the number to be squared rooted :"))
#let's assume the initial root be 0
x= 20
while (abs(x**2-n)>0.00001):
    x = x - ((x**2-n)/(2*x))
    print("result:the square root of {n} is {x}")
