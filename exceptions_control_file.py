try:
    file = open('testfile.txt', 'r')
    file.write("This is my test.file for exception handling!!")
except IOError:
    print('Error: can\'t find file or read data')
else:
    print('Written conntent inn the file successfully')
