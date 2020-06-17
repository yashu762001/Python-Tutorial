"""
TOPICS TO BE DISCUSSED:
1. INSTANCE METHODS.
2. GETTTERS AND SETTERS METHODS.
3. CLASS METHODS.
4. STATIC METHODS.

POINT TO BE REMEMBERED: CLASS VARIABLES AND STATIC VARIABLES WERE ONE AND THE SAME THING.
BUT CLASS METHODS ARE DIFFERENT ARE DIFFERENT AND STATIC METHODS ARE DIFFERENT.
"""
#  INSTANCE METHODS ARE THE ONES WHICH ARE DEPENDENT ON THE INSTANCES.THIS MEANS THAT WE NEED INSTANCES TO CALL
# METHODS. THESE METHODS ARE OBJECT DEPENDENT.

class Student:
    school = "Bikaner Boys School"
    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def average(self):
        print((self.m1+self.m2+self.m3)/3)

    def get_m1(self):
        print(self.m1)

    def get_m2(self):
        print(self.m2)

    def get_m3(self):
        print(self.m3)

    def set_m1(self,value):
        self.m1 = value
        print(self.m1)

    def set_m2(self,value):
        self.m2 = value
        print(self.m2)

    def set_m3(self,value):
        self.m3 = value
        print(self.m3)

    @classmethod
    def school_info(cls):
        print(cls.school)

    @staticmethod
    def info():
        print("Welcome to the Student Class!!!")

# print(__name__)
#
# s1 = Student(34,67,98)
# s2 = Student(45,65,98)
# s1.average()
# s2.average()
# s1.get_m1()
# s1.get_m2()
# s1.get_m3()
# s2.get_m1()
# s2.get_m2()
# s2.get_m3()
# s1.set_m1(98)
# Student.school_info()
# Student.info()


# Acessor Methods are used for fetching the values for objects. One way is to use object.the variable but if we
# want to make methods for this purpose. Then we have a method named getters methods.

# Similarly to set the original values of instances we can create setters method.
# Since all these methods are object dependent so these are called as the instance methods.

# Now if we want to access the class variables one way is to use objects.classvariable.
# But we don't want to do above since these variables are not object dependent.
# So there should exist a method independent of the object and yet able to print information about the class
# variables. Such methods which are independent of the instances but dependent on the class variables are called
# the class methods.

# if(__name__=='__main__'):
#     Student.info()

