x =int(input("enter the number x:"))
if (x%2 ==1 and x<=20):
    print("both conditions are setisfied")
elif(x%2 == 1 and x>20):
    print("first condition setisfied but second not")
elif(x%2 == 0 and x<20):
    print("second condition setisfied  but first not")
else:
    print(" both conditions are not setified")
    
