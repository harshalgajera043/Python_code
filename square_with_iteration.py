x=input('Enter the number x ')
x=int(x)
ans=0
remaining_iter = x
while (remaining_iter != 0):
    ans = ans + x
    remaining_iter = remaining_iter - 1
print('Square of',x,'is:',ans)
