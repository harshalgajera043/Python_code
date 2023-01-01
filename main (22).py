# #functions
# #docstrings
# def format_name(f_name,l_name):
#     """will going to return the fromated user name."""
#     firstname = f_name.title()
#     lastname = l_name.title()
#     return f"{firstname} {lastname}"

# print(format_name("harshaL","GajerA"))

#calculator final project

def add(n1,n2):
    """This function will going to add a number n1 into the number n2."""
    return n1+n2

def substract(n1,n2):
    """This function will going to substract a number n1 from the number n2."""
    return n1-n2

def multiple(n1,n2):
    """This function will going to multiple the number n1 and n2."""
    return n1*n2

def divide(n1,n2):
    """This function will going to divide a number n1 by a number n2."""
    return n1/n2

number_1 = float(input("Enter a number.\n"))

further_calculation = True
while further_calculation:
    operation = input("What operation would you like to perform on both the number?\n+\n-\n*\n/\n")
    number_2 = float(input("Enter a second number.\n"))
    if operation == "+":
        result  = add(n1=number_1, n2=number_2)
    elif operation == "-":
        result = substract(n1=number_1, n2=number_2)
    elif operation == "*":
        result = multiple(n1= number_1, n2=number_2)
    elif operation == "/":
        result = divide(n1=number_1 , n2=number_2)

    keep_calculating = input("do you want to keep going with result? press'y' for yes and 'n' for no.\n")
    if keep_calculating == "n".lower():
        further_calculation = False
        print(f"final result is {result}.")
    else:
        number_1 = result
