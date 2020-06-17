'''
TOPICS TO BE DISCUSSED:
1. DUCK TYPING 2. METHOD OVERLOADING AND METHOD OVERRIDING
'''

# class Laptop:
#     def code(self,ide):
#         ide.execute()
#
# class Pycharm:
#     def execute(self):
#         print("Compiling")
#         print("Running")
#         print("Spell Check")
#         print("Coloring Code")
#         print("Telling About Errors And Warnings")
#         print("Terminal")
#         print("Automatically Saving the code at the time of running")
#
# class Eclipse:
#     def execute(self):
#         print("Compiling")
#         print("Running")
#         print("Spell Check")
#         print("Highlighting errors in the line")
#         print("Console")
#         print("Need to Save File Before Execution")
#
# class CodeBlocks:
#     pass
#
#
#
# ide = Pycharm()
# Lappy = Laptop()
# ide = Eclipse()
# Lappy.code(ide)

# There is a famous saying that if you walk like a duck, run like a duck, swim like a duck , then you can be a duck.
# The meaning of above proverb is very deep. It means that the name,place,animal or thing whichever you behave like
# you become that.

#  We are using the same concept above. It says that if you have a laptop you can code but you need to have a ide
# installed in your laptop. The ide is also special since it should possess an execute method.

# The same thing we used in above code that ide could be pycharm or eclipse doesn't matter but should have  a execute
#  method within it. So initially we made ide to be object of Pycharm and since it had execute method it ran
# successfully.

# The object which belonged initially to a particular class is not fixed to become object of some other class.
# This is what polymorphism is since the object can behave like multiple class objects.

# So the concept is that if your class object possess a particular feature which i am searching for then i can use
# it as object of any class.

#  This is how the word polymorphism is made true by the variable behaviour of a object.

# This phenomenon is called DUCK TYPING.

'''  OPERATOR OVERLOADING '''

# a = 5
# b=6
# print(a+b)
# print(int.__add__(a,b))

# class Student:
#     def __init__(self,m1,m2):
#         self.m1 = m1
#         self.m2 = m2
#
#     def __add__(self, other):
#         a = self.m1+other.m1
#         b = self.m2+other.m2
#         temp = Student(a,b)
#         return temp
#
#     def __gt__(self, other):
#         a = self.m1+self.m2
#         b = other.m1+other.m2
#         if(a>b):
#             return True
#         else:
#             return False
#
#
# obj1 = Student(87,65)
# obj2 = Student(98,35)
# # print((obj1+obj2).m1)
# if(obj1>obj2):
#     print("obj1 is better than obj2 in studies")
# else:
#     print("obj2 is better than obj1 in studies")

# Let's go back two code for adding two numbers. We think that a and b declared above are numbers which are directly
# added but actually they are not numbers. They are actually objects. Once their type is known then the plus
# operator calls the add method corresponding to the class they belong to.

# So behind the addition a __add__method is getting called. This method has fixed object types. That is either
# int and int or int and float or float and float or char and char.

# But when we wrote add operator for two objects of type Student. Again the same add method was called but now the
# type of objects it got as argument were unknown to it. So the compiler threw error, that this type is unknown.

# But still we want to do this. So How to do this?

# Answer is operator overloading. This means that if the arguments we are providing are unknown to the method,
# so lets get the method known to this class. Now how can this thing be achieved?

# Again answer is very simple. You just have to redeclare the same method within your class. Define the way you
# want. So as we have done above.

# Now question arises how this topic comes under polymorphism. The answer is polymorphism means different behaviour
# of same thing. So here method is still the same but the way it is behaving is over us.

# So this was all about operator overloading. Read this concept carefully since it is very important.
# Whenever you work on a project you import lots of packages. But the functions defined there works the way
# they were made to. But we want the same function to work differently. How can this be done is by method overloading
# or if certain operator is designed for calling a function and we want the operator to work on objects belonging
# to my class also then you will need to redefine the method within the class you are using.

# One more thing to note is that in operator overloading the operator remains the same but the operands change.

''' METHOD OVERLOADING AND METHOD OVERRIDING  '''
# If I talk in terms of JAVA then method overloading means to use the name of function which is already defined
# but i will be changing the arguments. Either the number of arguments or the kind of arguments.

# But such a thing can't be done in python. The only thing possible in python is to declare a new function or
#  update the existing one.

# class Animal:
#     def sound(self):
#         print("Animals make sounds out of mouth")
#
# class Dog(Animal):
#     def sound(self):
#         print("Dog barks")
#
# class Lion(Animal):
#     def sound(self):
#         print("Lion groans")
#
# a1 = Animal()
# d1 = Dog()
# l1 = Lion()
# a1.sound()
# d1.sound()
# l1.sound()

# So in above example there is animal class which is a parent class and has lots of children classes out of which dog
# and lion are declared. In animal class there is a method named sound(). This method states that animals can make
# sounds. But the kind of sound made by dog and lion are different. So if i don't redeclare the method in their
# class then their objects will call the already present sound() method. Due to this we can't find out the difference
# between the objects of dog and cat. So to achieve this thing we declare the method according to us within these
# children classes and when their objects call this method the output is according to the way method is defined
# within them.

#  THIS CONCEPT OF REDEFINING METHOD OF PARENT CLASS WITHIN THE CHILDREN CLASS IS CALLED METHOD OVERRIDING.



