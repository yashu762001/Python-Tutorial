'''
Some Basic Mathematical Operations On Arrays
'''

from numpy import *
arr = array([1,3,4,6,9])
# print(arr,arr.dtype)
# arr = arr+5
# print(arr,arr.dtype)
# arr = (arr-5)*0.2
# print(arr,arr.dtype)
# arr = sin(arr)
# print(arr,arr.dtype)
# arr = log(arr)
# print(arr)
# print(arr.min())
# print(arr.max())
# arr1 = array([3,9,8,7,6,9])
# arr = arr+arr1
# print(arr)

# You can't add two arrays of different sizes. Very Obvious thing I feel yet need to be mentioned.

# arr1 = array([1,2,3,4,5])
# arr = arr*arr1
# print(arr)

'''
Copying Of Arrays
'''
# arr1 = arr
# print(arr1)
# print(id(arr))
# print(id(arr1))

# The address of both is same. This means no new array is created actually both are pointing to same locations.

# arr1 = arr.view()
# print(arr1)
# arr[0] = 2
# print(arr)
# print(arr1)
# print(id(arr))
# print(id(arr1))

#  So a new array with copied values has been formed at a different location within the memory.
# But when we update the values in the first array the same change is also reflected in the copied version also.
# So we created new array so as to keep the previous values safe and now start using the values of the original
# array. But this is not safe here since copied version will update along with the original array

# To prevent this we use copy method which helps us in this situation and once copied it separated itself from
# previous array which means now they are not related so if you change one of them the other one remains as it is.

# arr1 = arr.copy()
# arr[0] = 2
# print(arr)
# print(arr1)
# print(id(arr))
# print(id(arr1))

