'''ATM MACHINE CODE '''

from Errors import file1
from file1 import *

AccountBalance = 5000
try:
    v = int(input("Enter any 2 digit number"))
    if(v>=10 and v<100):
     print("Welcome to the State Bank Of India")
     print("For Debiting money click here")
     print("Debit from Current or Savings")
     DebitAmount = int(input("Enter the amount to be debited"))
     if(DebitAmount-AccountBalance<=0):
        print("Please don't press cancel while your transaction is going on")
        print("Your Transaction completed Successfully")
        print("Your remaining Account Balance is ",-DebitAmount+AccountBalance)
        print("Thank You for Using The Bank Service")
        print("Account Closes")
     else:
        raise BankingError
    else:
        raise NumberException

except ZeroDivisionError as e:
    print("Division By Zero is not Possible ",e)

except ValueError as e:
    print("Wrong Input", e)

except BankingError as e:
    print("Please don't press cancel while your transaction is going on")
    print("Sorry Your Transaction Failed")
    print("Your Account does not have sufficient balance")
    print("For checking Account Balance Click the icon below")
    print("If want to terminate the transaction click below")
    print("Thank You for using the bank Service")
    print("Account Closes")

except NumberException as e:
    print("Enter a Valid Two digit Number")
except Exception:
    print("Something went wrong")

print("Bye")