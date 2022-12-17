print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
if height >=120:
  age = int(input("what is your age?"))
  if age<=12:
    print("your ticket is $5.")
  elif age<=18:
    print("Your ticket is $7.")
  else:
    print("Your ticket is $12.")
else:
  print("Sorry you  can't ride the rollercoaster.")