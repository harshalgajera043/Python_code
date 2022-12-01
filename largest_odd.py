x=81
y=90
z=15
dx=-1
dy=-1
dz=-1
ans=-1


if x%2==1:
    dx=x
if y%2==1:
    dy=y
if z%2==1:
    dz=z

if (dx > dy or dy == -1) and (dx > dz or dz == -1):
    ans = dx
elif (dy > dx or dx == -1) and (dy > dz or dz == -1):
    ans = dy
elif (dz > dy or dy == -1) and (dz > dx or dx == -1):
    ans = dz
if ans != -1:
    print(ans,"is the largest odd number")
else:
    print("There is no odd number entered")
