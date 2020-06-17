"""
DIFFERENT WAYS OF CREATING ARRAYS IN NUMPY:
1.array - You give our random input as a list and can store all values not particular type.
2.linspace - Divides the start and end into 3rd input parts using formula (end-start)/parts-1.
3.arange - It adds values in array with different between consecutive values as the 3rd input.
4.zeros - All values will be 0 in the array. You only need to specify length of array. By default all values will
be float but if you want them to be int then after giving size as input also write int.
5.ones - same as zeros except that all elements are 1.
"""

from numpy import *
# arr = array([1,2,3,4,5.09],int)
# print(arr)
# print(arr.dtype)
# print(arr[0])

#  The major difference between creating arrays using numpy package and array package is that there we were needed
#  to provide the type of data but here we don't need to specify type of data. If one of the data is changed all
#  data is made of that particular type. for eg: in above example initially all elements were integers, then we
#  changed one entry to a floating point decimal. So now when we called the dtype function it returned that all
#  elements are of float type.

# arr = array([1, 2 ,3.09 ,5],float)
# print(arr)
# print(arr.dtype)

# arr = linspace(0,15,20,int)
# print(arr)

# arr = linspace(0,16,10)
# print(arr)

# arr = linspace(1,16,100)
# print(arr)

# arr = linspace(1,2)
# print(arr)

#  The linspace works using this algorithm: (stop-start)/steps-1
# So linspace was actually dividing into the number of values given as a 3rd input

arr = arange(1,14,3)
print(arr)

# In arange the 3rd input is not the number of parts i have to create in between start and stop. Here it means that
# we need firstnumber+3rdinput will be second input and this will go on until the number becomes less than equal
# to stop number.

# arr = zeros(5,int)
# print(arr.dtype)

# arr = ones(5,int)
# print(arr)

