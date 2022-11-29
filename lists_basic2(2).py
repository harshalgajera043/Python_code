Uni1 = ['PDPU', 'UNSW']
Uni2 = [['MIT', 'Caltech'], ['Harvard', 'Yale', 'Brown']]
Uni3 = ['PDPU', 'UNSW']

print('Uni1 =', Uni1)
print('Uni2 =', Uni2)
print('Uni3 =', Uni3)
print('Comparing Uni1 and Uni2: ',Uni1 == Uni2)
print('Comparing IDs of Uni1 and Uni2: ',id(Uni1) == id(Uni2))
print('Comparing Uni1 and Uni3: ',Uni1 == Uni3)
print('Comparing IDs of Uni1 and Uni3: ',id(Uni1) == id(Uni3))

print('\n')

for ele in Uni2:
    print('Uni2 contains',ele)
    print(' which contains')
    for u in ele:
        print(' ', u)

if 'PDPU' in Uni1:
    print('PDPU is in Uni1 list')
