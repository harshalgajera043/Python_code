def removeDups(L1,L2):

    for e1 in L1:
        if e1 in L2:
            L1.remove(e1)
L1 = [30,10,90,"PDPU",100]
L2 = [30,10,20,80]
print("L1=",L1)
print("L2=",L2)
removeDups(L1,L2)
print("After removing duplicates L1=",L1)
print("not  a correct answer->10 is still there in L1")

def removeDups(L1, L2):
    for e1 in L1[:]: 
        if e1 in L2:
            L1.remove(e1)
L1 = [30, 10, 90, 'PDPU', 100]
L2 = [30, 10, 20, 80]
removeDups(L1, L2)
print('after removing duplicates by clning L1 = ',L1)            