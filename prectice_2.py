#updated BMI calculator
Height = float(input("Enter your hegiht in m.\n"))
Weight = float(input("enter your weight in kg.\n"))

# let's calculate the BMI using equation!
BMI = Weight/Height**2
Round_BMI = round(BMI,2)
if Round_BMI<=18.5:
  print(f"Your bmi is {Round_BMI}, you are underweight.")
elif Round_BMI<=25:
  print(f"Your bmi is {Round_BMI}, you are normal.")
elif Round_BMI <=30:
  print(f"Your bmi is {Round_BMI}, you are slightly overweight.")
elif Round_BMI<= 35:
  print(f"Your bmi is {Round_BMI}, you are overweight.")
else:
  print(f"Your bmi is {Round_BMI}, you are overweight/obese.")