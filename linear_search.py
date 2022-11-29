def search(L, e):
    """assumes L is a list, the element of which are in 
    ascending order.
    returns true if e is in L and False otherwise"""
    for i in range(len(L)):
        if L[i] == e:
            return i
        else:
            return -1
            
Fruits = ['apple', 'banana', 'mango', 'cherry']    

element = input('enter the fruit name you want to search : ')

index = search(Fruits, element)

if (index !=-1):
    print('Fruit', element, 'is found in the list at position',index)
else:
    print('Fruit', element, 'is not found in the list')

print('Fruit', index )    
     
