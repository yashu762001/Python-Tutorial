# nums = [7,8,96,5]
# print(nums)
# for i in range(0,len(nums)):
#     print(nums[i],end=" ")
#
# print(" ")
# for i in nums:
#     print(i,end=" ")

# it = iter(nums)
# print(it)

# from array import *
# arr = array('i',[7,8,96,5])
# it = iter(arr)
# print(it)
# print(it.__next__())
# print(it.__next__())
# print(it.__next__())
# print(it.__next__())
# print(it.__next__())

# val = 1
# it = iter(val)
# print(it.__next__())
# print(it.__next__())
# print(it.__next__())

# val = (1,45,67,98)
# it = iter(val)
# print(it.__next__())
# print(it.__next__())
# print(it.__next__())
# print(it.__next__())

# class TopTen:
#     def __init__(self):
#         self.num = 1
#
#     def __iter__(self):
#         return  self
#
#     def __next__(self):
#         if(self.num<=10):
#          val = self.num
#          self.num+=1
#          return val
#
#         else:
#             raise StopIteration

# vals = TopTen()
# for i in vals:
#     print(i)
# This above code is automatically calling the method next and printing the result.
# This could be done the other way also, so no way to take tension if not understand above code.

# for i in range(0,10):
#     print(vals.__next__())

# This topic is not quite useful. But still Let's discuss.
# Iterators are used when we want to go through the list and find out what elements are present in it.
# We have a iter function which takes as input as a list and returns a iterator object. But if you print this object
# you will see a hexadecimal address on the screen. This is because the screen is showing the address where the
# iterator object is formed in the memory. To find the values we need to call the method ie next. This method keeps
# on printing the values present in the list and returns 1 value at a time.

# I have created a iterator above for my class TopTen. It overrides the function __iter__ to return a object of type
# student somewhere in the memory. Then to iterate we have a __next__ method. It iterates until value 10 is reached.
# If we want raise exception then it will print None since none value is there but if we want to stop after 10
# we need to raise a exception.

''' Generators '''
# def topten():
#     i=1
#     while(i<=20):
#         yield i*i
#         i+=1
#
# val = topten()
# for i in val:
#     print(i)


def hello():
    yield 5


a = hello()
print(a)

# This is same as iterators but slight difference is that we are saved from declaring functions like iter and next.
# Also we can see above code it prints address of values and to fetch value from it we need to use next method
# This is also defined above. Whenever we want to fetch values 1 at a time we can use generators since they won't
# terminate the loop. Whenever called will return the value.

'''  THIS IS NOT MUCH INTERESTING TOPIC YET HERE COMES THE END OF THIS TOPIC '''

'''  THIS WAS ALL ABOUT PYTHON PROGRAMMING LANGUAGE. NOW JUST PRACTICE AND MAKE REAL LIFE PROJECTS  '''
'''   ALSO START WITH MACHINE LEARNING AND DATA SCIENCE SINCE THAT IS THE FUTURE.'''
'''   IF YOU ARE INTERESTED IN APP DEVELOPMENT OR WEB DEVELOPMENT THEN START LEARNING DJANGO  '''




