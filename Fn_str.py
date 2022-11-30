def check(s1,s2):
    if(s2 in s1):
        return True
    else:
        return False
s1=input('Enter the string: ')
s2=input('Enter the Sub-string to be checked: ')
if(check(s1,s2)):
    print('s2=',s2,' is in s1=',s1)
else:
    print('s2=',s2,'is not in s1=',s1)