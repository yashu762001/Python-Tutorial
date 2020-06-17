# class A:
#     def func1(self):
#         print("Welcone to Class A")
#
#     def func2(self):
#         print("Welcome to Class A's Func2")
#
# class B(A):
#     def fun3(self):
#         print("Welcome to Class B")
#
#     def func4(self):
#         print("Welcome to func4 of Class B")

# a = A()
# a.func1()
# b = B()
# b.fun3()
# b.func1()
# b.func2

# Above is called Single Level Inheritance. So when a class inherits other class it is called the children class or
# the subclass and the class which it inherits features from is called the parent class or the Super class.

# class C(B):
#     def func5(self):
#         print("Welcome to Class C")
#
#     def func6(self):
#         print("Welcome to Func6 of Class C")
#
# c = C()
# c.func2()
# c.func1()
# c.fun3()
# c.func4()
# c.func5()
# c.func6()

#  If the family tree is there with more than 2 members then it is called MultiLevel Inheritance.

''' MULTIPLE INHERITANCE '''

# class A:
#     def func1(self):
#         print("Welcome to Class A")
#
#     def func2(self):
#         print("Welcome to func2 of Class A")
#
# class B:
#     def func3(self):
#         print("Welcome to Class B")
#
#     def func4(self):
#         print("Welcome to func4 of Class B")
#
# class C(A,B):
#     def func5(self):
#         print("Welcome to Class C")
#
#     def func6(self):
#         print("Welcome to func6 of Class C")
#
#
# c = C()
# c.func6()
# c.func5()
# c.func4()
# c.func3()
# c.func2()
# c.func1()

''' Constructors INHERITANCE AND SUPER KEYWORD AND METHOD RESOLUTION ORDER '''

# class A:
#     def __init__(self):
#         print("In The constructor of A")
#
#     def fun1(self):
#         print("Welcome to Class A")
#
#     def fun2(self):
#         print("Welcome to fun2 of Class B")
#
#
# class B(A):
#     def __init__(self):
#         print("In the constructor of B")
#         # super().__init__()
#         super().fun1()
#
#     def fun3(self):
#         print("Welcome to Class B")
#
#     def fun4(self):
#         print("Welcome to fun4 of Class B")
#
#
# # a = A()
# b = B()

# When object is created the constructor of class to which object belongs is called. If the class is extending a
# class and we have our own defined constructor then the output would be according to the way i have designed
# the constructor.

# But if the default constructor is called, then it will automatically call the constructor of super class and the
# output would be according to the way super constructor is designed.

# If we want to call the func of super class, one way is to use the object name.the funcname. The other way this
# can be done is by using superkeyword().funcname.

''' METHOD RESOLUTION ORDER '''

# class A:
#     def __init__(self):
#         print("In The constructor of Class A")
#
#     def fun1(self):
#         print("Welcome to Class A")
#
#     def fun2(self):
#         print("Welcome to fun2 of Class A")
#
# class B:
#     def __init__(self):
#         print("In the Constructor of Class B")
#
#     def fun1(self):
#         print("Welcome to Class B")
#
#     def fun2(self):
#         print("Welcome to fun4 of Class B")
#
# class C(B,A):
#     def __init__(self):
#         super().__init__()
#         print("In the Constructor of Class C")
#         super().fun1()
#
#     def fun5(self):
#         print("Welcome to Class C")
#
#     def fun6(self):
#         print("Welcome to fun6 of Class C")
#
# c = C()

# When a class inherits features from more than 1 classes, when lets say default constructor of class C is called
# then which super class constructor is going to be called (A or B) ,the answer is very simple:

#  The execution order follows left to right. Which left to right? The order in which you mention classes being
#  extended.

