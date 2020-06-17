# from abc import ABC , abstractmethod
#
# class Animal(ABC):
#     @abstractmethod
#     def sound(self):
#         pass
#
#     def walk(self):
#         print("Can Walk")
#
# class Dog(Animal):
#     def sound(self):
#         print("Dog barks")
#
# d1 = Dog()
# d1.sound()
# d1.walk()

# Like JAVA we can't declare any class as abstract. First we need to import Abstract Classes and Abstract Methods
# from abc package. After that the class which we want to be abstract like Animal in above case, has to be made
# children class of ABC class.

# Important point to note about Abstract class is that they can't be instantiated.
# We can declare abstract as well as non abstract methods in Abstract class.
# Reason for declaring abstract method is to prevent redefining the method in children class the way we want.
# We will just declare the abstract method but definition will be there in children class.
# Children class if wants to be instantiated need to override abstract method of parent abstract class.
# If would not override the abstract method , then children class will also become abstract and we would not be able
# to create objects of this class.

                        '''     THIS WAS ALL ABOUT OOPS.      '''