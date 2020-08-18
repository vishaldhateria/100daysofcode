# my__1D_array = numpy.array([1, 2, 3, 4, 5])
# print my_1D_array.shape     #(5,) -> 5 rows and 0 columns

# my__2D_array = numpy.array([[1, 2],[3, 4],[6,5]])
# print my_2D_array.shape     #(3, 2) -> 3 rows and 2 columns 

# change_array = numpy.array([1,2,3,4,5,6])
# change_array.shape = (3, 2)
# print change_array  
# print numpy.reshape(my_array,(3,2))

import numpy

def reshapeme(arr):
    reshar = numpy.array(arr,int)
    return numpy.reshape(reshar,(3,3))

arr = input().strip().split(' ')
print (reshapeme(arr))
