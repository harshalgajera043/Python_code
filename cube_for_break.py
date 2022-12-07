x = int(input('enter the integer:'))
for ans in range(0,abs(x)+1):
    if ans**3 >= abs(x):
        break
if ans**3 != abs(x):
    print(x,'is not a perfect cube')
else:
    if x<0:
        ans = -ans
    print('cube root of',x,'is',ans)
