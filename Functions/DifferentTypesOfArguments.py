'''
SO WHENEVER WE DEFINE A FUNCTION WE NEED TO GIVE IT SET OF ARGUMENTS.IN PYTHON THESE HAVE BEEN CATEGORISED INTO
4 TYPES:
1. POSITION
2. DEFAULT
3. KEYWORD
4. VARIABLE LENGTH
'''
''' POSITION ARGUMENTS: '''

# def details(name,age):
#     print("name is",name)
#     print("age is",age)
#
# details('yash',19)
# details(19,'yash')

# When you will run this code in 1 situation  name is printed as yash and in another situation name is printed as
# 19. Now a regular mindset states that name cannot be 19, even though "it's his choice."
# This shows that position of arguments affects the output. In some situations maybe possible that we have 1crore
# objects and each has to be provided with a data. Now we can't jumble the data since which data is to be accquired by
# which object is fixed. So we need to take care about the position of arguments.

#  THIS IS WHAT POSITION ARGUMENTS CONCEPT IS. NOT A ROCKET SCIENCE I FEEL.

""" KEYWORD ARGUMENTS: """

# def details(name,age):
#      print(name)
#      print(age)
#
# details(age=19,name='yash')

#  Let's say we were working on a project and already written 10000's of lines of code. Now i know that i defined
#  somewhere the function details and also know that it took 2 arguments:name and age. Bit i don't remember the
#  positions of arguments. In that case i will need to play safe. So i used a tactic: since i know variables so i
#  know which variable should get what value. So i used the variable name and gave them the values as you can see
#  int he above code.

#  THIS IS WHAT KEYWORD ARGUMENTS IS.

'''  DEFAULT ARGUMENTS: '''

# def details(name,age=18):
#     print(name)
#     print(age)
#
# details('yash')
# details('yash',age=28)
# details('yash',28)
# details(name='yash',age=28)
# details(28,'yash')

# So we gave a default value to the arguments. This means even if we forget to give values to the argument ,the code
# will not fail and use the default values provided. But if we want new value then do the same thing as done above.

#  THIS IS WHAT DEFAULT ARGUMENTS IS.

''' VARIABLE LENGTH ARGUMENTS: '''

# def add(x,y):
#     c = x+y
#     print(c)
#
# add(5,3,67,98)

# Error is noted since the function was expecting only two arguments and i gave 4 arguments. But the function should
#  be versatile. Whether i give 2 arguments or 4 or 6 it should print the sum.

#  HOW CAN WE ACHIEVE THIS VERSATILITY??

# def sum(*b):
#     c=0
#     for i in b:
#         c+=i
#     print(c)
#
# sum(23,45)
# sum(23,45,67)
# sum(23,45,67,100)

# So i think this versatility is achieved. I used a *before the variable which stored the entire list of arguments
#  in a tuple named b. Then i applied a for loop to take elements from the tuple and add them and store the sum
#  in a third variable. Finally we print The third variable.

#  THIS IS ALL ABOUT VARIABLE LENGTH ARGUMENTS.

#  Something Extra :

# def details(name,**extra):
#     print(name)
#     if len(extra)!=0:
#       print(extra)
#
# details('yash',age=19,color='Fair',quality='ProgrammingGeek')

#  So if we want to print like above we need to use keyword arguments.
#  But how to pass them as arguments??
#  We use ** which actually creates a dictionary for remaining elements with the keyword being the key value and
#  value assigned to it as the value of key. This creates a key value pair which is actually being printed.
