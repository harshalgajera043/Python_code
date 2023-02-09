year = int(input('Enter a valid year to be checked '))
if year % 400 == 0:
    print(year, "is a Leap Year")
elif year % 100 == 0:
    print(year, "is not a leap Year")
elif year % 4 ==0:
    print(year, "is a leap Year")
else:
    print(year, "is not Leap Year")
