# def modify(x):
#     x = 8
#     print(x)
#
# a = 10
# print("Before function calling",a)
# print("Calling Function")
# modify(a)
# print("After function calling",a)

# Some people say it to be pass by value and not pass by reference since a is not updated.
# Simple explanation which people think of is that somewhere within the memory value of a is copied and that copied
# value is updated. So it is pass By value. BUT IT IS WRONG CONCEPT!!!!!

# What Actually happens let's see:

# def modify(x):
#     print(id(x))
#     x = 8
#     print(x)
#     print(id(x))
#
# a = 10
# print(id(a))
# modify(a)
# print(a)
# print(id(a))

# Run above code and you will see the magic:
# Actually no copy of a is formed in the memory,x is pointing to the same memory location which a is pointing to.
# When i update the value of x,actually somewhere in the memory 8 is formed and this location is now pointed to by
# x. But a is still pointing to it's original location.
# Thus it is neither pass by value nor pass by reference according to this example.

# Let me consider one more example which will confuse you even more but interesting:

# def modify(list):
#     print(id(list))
#     list[2] = 36
#     print(id(list))
#     print(list)
#
# list = [2,67,98,100]
# print(id(list))
# modify(list)
# print(id(list))
# print(list)

# So on running this piece of code we find that originally both are pointing to same memory location,thus it can't
# be pass by value. But final output shows that changes are reflected in the original list,which means it is
# pass by reference.

# Moral Of the story is that function calling in python is not call by value and not exactly call by reference.
# It is something different, which no one knows.

# So people can we swap two variables using swap function?
# Answer is No but why do we need a function.
# For swapping python provides the easiest technique ie a,b = b,a .
