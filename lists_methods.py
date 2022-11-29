L1 = [20 , 10]
L2 = [90, 20, 80]

L = L1 + L2

print('L =', L)
L1.extend(L2)
print('L1=', L1)
L1.append(L2)
print('L1=', L1)



L3 = [20, 30, 50, 0, 10, 90, 30, 20]
print('L3 =', L3)
L3.sort()
print('sorted L3 ', L3)
print('count of 20 ',L3.count(20))
L3.insert(2, 80)
print('after inserting 80 at second index ',L3)
L3.remove(20)
print('after removing the first occurence of 20 ',L3)
print('index of 20 ',L3.index(90))
L3.pop(3)
print('after poping the element at 3rd index ',L3)
L3.reverse()
print('after reversing list ',L3)
