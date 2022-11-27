import pylab
principal = 1000
interestRate = 0.07
years = 10
values = []
for i in range(years + 1):
    values.append(principal)
    principal += principal*interestRate
pylab.rcParams['lines.linewidth']
pylab.plot(values)
pylab.plot(values, 'ro')
pylab.title('7 percent Growth, compound Annually',fontsize = 'xx-large')
pylab.xlabel('Years of Compounding')
pylab.ylabel('Value of principal (Rs.)')
pylab.show()
