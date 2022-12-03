def findAnEven(l):
    for i in l:
        if i%2 == 0:
            return i
    raise ValueError('l does not contain an even number')
l=[1,9,3,5,7,8]
ans=findAnEven(l)
print('First even number: ',ans)
    
