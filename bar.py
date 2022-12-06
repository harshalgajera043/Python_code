import pylab as p
subjects = ['c', 'c++', 'Java', 'Python', 'PHP']
students = [23,17,35,39,12]
p.title('Students enrolled in year 2020')
p.xlabel('Subjects')
p.ylabel('Number of students')
p.bar(subjects,students)
p.show()