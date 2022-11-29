L = [x**2 for x in range(1, 7)]
print('the newly generated list is: ',L)


#mixed list

mixed = [1, 2, 'a', 3, 4.0]
print('new list after operation on the mixed list (squaring only integers):',[x**2 for x in mixed if type(x) == int])
print('mixed list is: ',mixed)