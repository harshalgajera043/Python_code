Dict1 = {}
print('empty dictionary: ')
print(Dict1)

#dict2

Dict2 = {11: ' PDPU', 22: 'Gandhinagar', 33: 'Gujarat', 44: 'India'}
print('\nDictionary with the use of integer keys: ')
print(Dict2)
print('Dict2 keys: ',Dict2.keys())
print('Dict2 values: ',Dict2.values())
print('Dict2 length: ',len(Dict2))
print('is 44 in Dict2: ',44 in Dict2)
Dict2[55] = 'asia'
print(Dict2)
print('the value with key 22 is: ',Dict2[22])


#for dict3

Dict3 = {'name' : 'PDPU', 1: [1, 2, 3, 4], 8: 'Gujarat'}
print('\nDictionary with the use of mixed keys keys: ')
print(Dict3)
print('Dict2 keys: ',Dict3.keys())
print('return Dict3[8]: ',Dict2.get(8))
del(Dict3[1])
print('after deleting pair with key 1',Dict3)
for k in Dict3:
    print('key is: ',k)

