batch = [40, 26, 39, 30, 25, 21, 49]
cut = 25
for i in batch:
    assert i >= 25, 'This batch is Rejected'
    print(i, ' is O.K')
    
