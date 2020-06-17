'''
Concept of Functions was brought to reduce the task of writing similar codes repetitively.
'''

# def add_numbers(x,y):
#     answer = x+y
#     print(answer)
#
#
# z=add_numbers(2762746,857397594)
# print(add_numbers)
# print(z)

# In this function if we will return nothing then the value stored in variable z is None, which is quite obvious.
# Otherwise if it is returning certain value then we will need a variable to store the returned value.

# def square(x):
#     print(x*x)
#
# z = square(70)
# print(square)
# print(z)

# So on printing the name of function we actually got a random hexadecimal value. This value is actually the
# address of function object.
# If you would have studied JAVA programming then we create objects to call functions and here the function itself
# is a object. So this is a new concept which states that python function is a object.
# The value returned by the function is actually the value stored in the object. So if value returned by the
# function is none then it means value stored in function object is None.

# def power(a,b):
#     count = a
#     for i in range(1,b):
#         count*=a
#     return count
#
# z = power(69,69)
# print(power)
# print(z)

# In JAVA we need to create a object of BigInteger Class to compute such big powers but python allows us the
# simplicity by allowing us to write same piece of code for large as well as smaller values.

# count = 1
# def temp(x):
#     global count
#     x+=count
#     count = count+x
#     return x
#
# z = temp(6)
# print(count)
# print(z)

# The variables declared inside a function have their scope restricted to the function.
# Th variables declared outside the function can be used within the function but can't be modified until and
# unless we define them as global within the function.
# Outside variable can't be declared global by using global keyword since it's scope is within the complete class
# This is actually not a variable but a object since everything in python is a object.


