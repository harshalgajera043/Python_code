x = int(input("number of blue balls :"))
y = int(input("number of red balls :"))
if (x <=30 and y <= 20 and x+y==40):
    print("probability of x=",x/(x+y))
    print("probability of y=", y/(x+y))
else:
    print("pronability is zero")
