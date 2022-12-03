numSuccess = float(input("enter number of Successs: "))
numFailures=float(input("enter the number of failures: "))
try:
    successFailureRatio = numSuccess/float(numFailures)
    print("the Success/Failure ration is",successFailureRatio)

except ZeroDivisionError:
    print("no Failures. so the success/Failure ratio is undefined.")
print("this is the End of the proogram")
