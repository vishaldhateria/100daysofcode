import numpy 
# The NumPy (Numeric Python) package helps us manipulate large arrays and matrices of numeric data.

# a = numpy.array([1,2,3,4,5])
# print a[1]          #2

# b = numpy.array([1,2,3,4,5],float)
# print b[1]          #2.
#watch the python code with nodemon it is a generic tool to watch the code and rerun on detecting any changes in it.
# Steps
# npm -g install nodemon 
# nodemon filename.py
inputar = '12 1 -1 -2 -3'.strip().split(' ')

def arrays(arr):
    # complete this function
    # use numpy.array
    return (numpy.array(arr[::-1],float))
print(arrays(inputar))


