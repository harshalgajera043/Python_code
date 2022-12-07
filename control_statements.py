s= input("enter the string :")
for c in s:
    if (c == "$"):
        continue
    elif (c == "!"):
        pass
        print("it is !")
    elif (c == "."):
        break
    print('current character:',c)
