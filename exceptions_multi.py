def readVal(valType, requestVal, requestDiv):
    val = input(requestVal)
    div = int(input(requestDiv))
    try:
        val = valType(val)
        print("Val/div",val/div)
        print("2 + '3'",2+"3")
    except(ValueError,TypeError):
        if ValueError:
            print("Value error")
        elif TypeError:
            print("Type error")
    except ZeroDivisionError:
        print("Exception: value of div is zero")
readVal(int, 'enter an integer: ','enter a non-zero value: ')
