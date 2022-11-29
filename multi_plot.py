import pylab
x = ['feb', 'mar', 'apr']
y1 = [205, 190, 63]
y2 = [5, 130, 605]
pylab.title('Comparing deaths by accident and by COVID199 for city Ahmedabad in 2019')
pylab.plot(x, y1)
pylab.plot(x, y2)
pylab.xlabel('Month')
pylab.ylabel('Number of deaths')
pylab.legend(["Accidents", "COVID19"])
pylab.show()