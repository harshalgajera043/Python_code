start = int(input('Enter the starting number'))
stop = int(input('Enter the highest number'))
step = int(input('Enter the step size'))
for i in range(start, stop, step):
    print(i)
print('With default step value')
for i in range(start, stop):
    print(i)
print('With default start and step values')
for i in range(stop):
    print(i)
print('Test1: whether changinh the value of stop makes any difference')
stop=5
for i in range(stop):
    for j in range(stop):
        print(j)
        stop = 3
print('With specific sequence to be iterated over')
for i in [10,35,48]:
    print(i)
    
