def printName(firstName, lastName, reverse):
    if reverse: 
        print(latname + ', ' + firstName)
    else:
            print(firstName, lastname)
def printName(firstName, lastName, reverse = False):
    if reverse:
        print(lastName + ', ' + firstName)
    else:
            print(firstName,lastName)
printName('Rutvij','Jhaveri',True)
printName(lastName='Jhaveri',firstName='Rutvij',reverse=True)
printName('Rutvij','Jhaveri')
printName('Rutvij','Jhaveri',reverse=True)
