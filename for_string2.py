total = 0
s = '8.34,35.5,34.64,34.56,2,46.5'
for c in s.split(','):
    total = total + float(c)
print('the total of the digits is ',total)
