a=15
a=a+10
print("value of a before calling any function:",a)

def change1():
    global a
    a=a+5
    print("value of aa inside a function:",a)

def change2():
    global a
    a=a+10
    print("valye of a inside a function:",a)

change1()
print("value of a outside a function:",a)
change2()
print("value of a outside a function:",a)
