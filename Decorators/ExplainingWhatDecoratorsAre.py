# def div(a,b):
#     print(a/b)

# div(4,2)
# div(2,4)

#  Now i want whatever be the order of input, the output should be the same.
# This means output for div(2,4) and div(4,2) both should be 2.
# One way to achieve this this thing is to put a if condition in the original function.

# def div(a,b):
#     if(a<b):
#         a,b = b,a
#
#     print(a/b)
#
# div(2,4)
# div(4,2)

# So we have successfully achieved what we wanted.
# But if we don't have the access to the function, then what can we do.
# I mean that in most cases we just import the functions from the packages, but what if we want to add extra
#  features to them. To solve this issue we have the concept of Decorators.

#  DECORATORS HELP IN ADDING EXTRA FEATURES TO THE FUNCTION.

def div(a,b):
    return (a/b)


def smart_div(func):
    def inner(a,b):
        if(a<b):
            a,b = b,a

        return func(a,b)

    return inner

div = smart_div(div)
z = div(2,4)
print(z)
div(18,64)
div(98,49)

#  Let's consider a example that we have a robot which can only walk and we want it to run also. So we go to a
#  consultancy firm and they give us the address of a repair shop. We go to the repair shop and they make certain
#  changes and calls the previous shop which created it to give it the final finishing and return the final
#  product.

#  Above example is exactly how the decorators work in python.
#  In above code the smart_div method is actually the consultancy firm where we took our robot. This function
#  returned the address of the modified division method that is the inner function. The inner function did changes
#  and called the old division method to return the final answer.
#  Now during calling the company our div actually stored the address of old division object. Now after calling
#  company it stores the address of modified division object. So on assigning values to new div object we are
#  actually giving values to the modified division which d changes and calls the old division method for printing
#  the result. Although we can use print method in repair shop also to do but doesn't matter whosoever do it.

#  THIS TAKES US TO THE END OF CONCEPT OF DECORATORS. TRY TO FEEL THAT FUNCTION IS A OBJECT. ONLY THEN YOU
#  CAN UNDERSTAND HOW DECORATORS WORK.