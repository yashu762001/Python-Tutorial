'''
A very basic 'for' loop for printing numbers from 1 to 6
'''
# for i in range(1,7):
#     print(i)
# Important point regarding range(x,y): The variable can take the values less than y and greater than equal to x

'''
Way to print numbers present in a list
'''
a = [1,2,4,7,9,23,75479]
# for i in a:
#     print(i)

# This is also the way we print elements of a list in java programming. There it was called the for each loop

'''
Another method for printing elements of a list in python 3
'''
# for i in range(0,7):
#     print(a[i])

# If we know the exact number of iterations then prefer using for loop else use while loop

'''
Print table of 23
Another application of for loop
'''
# for i in range(1,11):
#     print("23*"+str(i)+" = "+str(23*i))

'''
Printing tables of all numbers from 1 to 10
'''

# for i in range(1,11):
#     for j in range(1,11):
#         print(str(i)+"*"+str(j)+" = "+str(i*j))
#     print(" ")

'''
Another Interesting Example for printing pattern of stars.
'''

# stars=6
# for i in range(0,6):
#     for j in range(0,stars-i-1):
#         print("",end=" ")
#
#     for j in range(0,i+1):
#         print("*",end="")
#
#     print(" ")