'''
WORKING OF MATRICES:
Topics Covered:
1. How are Matrices Created?
2. How to convert 2D array to 1D array?
3. How to convert 2D array to 3D array?
4. How to add,subtract,divide,multiply two matrices?
5. How to print diagonal elements of a 2D square matrix?
6. How to find minimum and maximum elements in matrix?
'''

from numpy import *
arr = array([[1,2,4],[2,4,5,]])
print(arr[1][1])
# print(arr)
# print(arr.ndim)
# print(arr.size)
# arr1 = arr.flatten()
# print(arr1)
# arr = arr.reshape(2,3)
# print(arr)
# arr = arr.reshape(3,,21)
# print(arr)
# print(arr.ndim)
# print(arr.size)
# arr = array([1,2,4,2,4,5])
# arr = arr.reshape(2,3)
# print(arr)
# print(arr.size)
# print(arr.dtype)
# print(id(arr))
# print(arr.ndim)


arr = array([1,2,4,2,6,5,8,3,9])
arr = arr.reshape(3,3)
# print(arr)
m1 = matrix(arr)
# print(m1)

# print(m1)
# arr1 = array([2,4,6,7,8,1,2,3,4])
# arr1 = arr1.reshape(3,3)
# arr2 = arr1*arr
# print(arr2)
# m2 = matrix(arr1)
# print(m2)
# m3 = m1*m2
# print(m3)

a,b = len(arr),int(arr.size/len(arr))
# print(a,b)



# for i in range(0,a):
#     for j in range(0,b):
#         print([i][j],end = " ")
#
#     print(" ")

# print(diagonal(m3))
# print(m3.max())

#  This takes us to the end of Numpy package in python.

a = int(input("Enter the first number"))
b = int(input("Enter the second number"))

t = a%b
while(t!=0):
    z = a%b
    a = b
    b = z
    t = a%b


print(b)

# while(t!=0):
#
#     x =