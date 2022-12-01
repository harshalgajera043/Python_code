#python program showing to modify a global value without using global keyword

a = 15 # global variable a

#function to change a global value
def change():
        global a # Remove the comment and comment the below line: 'a' is made global
        a = 5 # Remove the comment and comment the above line: if above statement is not written
        a = a + 5
        print(a)

change()
print("Value of a outside the function :",a)
