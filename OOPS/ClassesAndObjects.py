'''
TOPICS DISCUUSED:
1. WHAT ARE CLASSES AND OBJECTS?
2. HOW TO DECLARE CLASSES AND OBJECTS?
3. CONCEPT OF CONSTRUCTORS AND SELF KEYWORD?
4. DIFFERENCE BETWEEN CLASS VARIABLES AND INSTANCE VARIABLES?
'''

# Classes are the blue print design. What does it even mean?
# A class is like a community which share similar attributes and qualities.
# A class doesn't occupy space because it is just a concept. Now to follow all the above qualities and attributes
# we want someone physically available and occupying space. These real life entities belonging to a class are called
# the objects.
class Account:
    RateOfInterest = 7
    def __init__(self,AccountNumber,Name,Deposit,Balance):
        self.AccountNumber = AccountNumber
        self.Name = Name
        self.Deposit = Deposit
        self.Balance = Balance

    def hello(self):
        print("Welcome To The State Bank Of India!!")

    def Maintain(self):
        self.Balance = self.Balance+self.Deposit

    def Debit(self,amount):
        if(amount>self.Balance):
            print("Insufficient Balance In Account")
            print(self.Balance)
        else:
            print("Click Here To Confirm Transaction")
            print("Your Transaction Occured Successfully")
            print("Your Remaining Balance is ",self.Balance-amount)
            self.Balance = self. Balance - amount

obj1 = Account("2324435","Yash",7,40000,2500)
obj2 = Account("2344355","Ira",8)

obj1.hello()
print(obj1.AccountNumber)
print(obj1.Name)
print(obj1.RateOfInterest)
obj1.Maintain()
print(obj1.Balance)
obj1.Debit(5000)
print(obj1.Name)

print(obj1.RateOfInterest)

#  Everywhere we see self . What is it?
#  So actually the python is designed in such a manner that every operation is to be done on the object.
#  So by default argument any function has is the object that is the self.

# In above code we defined two different types of attributes. Attributes like Name,AccountNumber,Balance are
# dependent upon the objects associated with the class.
# But the variable RateOfInterest is fixed for all object which means this attribute will remain the same for all
# objects.

# This above concept leads us towards a newer theory that is Instance Variables and Class Variables.
# Instance Variables are the ones which are object dependent.
# Class Variables are the ones which are class dependent which means their value will remain the same for all the
# real life entities belonging to the class.

# Instance Variables can be modified using the object name.
# Class Variables can be modified using the class name.

# Don't define the class variables inside the constructor. Always define them outside the constructor.