class Student:
    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno


    def show(self):
        print(self.name,self.rollno)

    class Laptop:
        def __init__(self,brand,cpu,ram):
            self.brand = brand
            self.cpu = cpu
            self.ram = ram

        def show(self):
            print(self.brand,self.cpu,self.ram)


# s1 = Student('Navin',2)
# s2 = Student('Yash',49)
# # print(s1.name,s2.name)
# s1.show()
# obj = Student.Laptop('Hp','i7','8gb')
# obj1 = Student("yash",56)
# obj2 = obj1.Laptop('Hp','i5','8GB')
# print(id(obj1))
# print(id(obj2))
# obj2.show()

#  We can create object of inner class . But just like JAVA we don't need to create object of outer class to create
#  object of inner class. To create object of inner class we just need to access the name of outer class since this
#  class Laptop is only visible to the ones who are member of Student Class.

#  Inner Classes are created only when we want That this particular class should be visible to this particular class.
#  So Here only Student class objects have access to Laptop class. We can't directly use Laptop class name to create
#  object. We need to take use of Student class Since where is this class Present. Answer is Student Class.

obj = Student("yash",49)
print(type(obj))

if(type(obj)=="'__main__.Student'"):
    print("Welcome To Student Class")