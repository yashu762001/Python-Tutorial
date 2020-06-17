# var = open('info.txt','r')
# var1 = open('hello.txt','w')

# var1.write(var.read())
# var1.close()
# var1 = var.read()

#  This variable object is storing the information present in the file.
#  If you familiar with the concept of pointers then here this variable var is actually a pointer to this file.
#  Basically it stores the address of location where this file is present or created in the memory.
# when we use read function it actually takes the reference object that is the var and starts executing reading
# and whatever is read is stored in another object variable that is var1.

# print(var1)
# var.close()

# var = open('tagger.txt','r')
# var1 = var.read()
# print(var1,end=" ")

'''
The files present in the pycharm projects folder can only be handled here.
'''

var = open("C:/Users/ranu hp/Desktop/tagger.txt",'w')
temp = "\n I want to make a very successfull company worth billion dollars.\n"
var.write(temp)
var.close()

var = open("C:/Users/ranu hp/Desktop/tagger.txt",'r')
# print(var.read())
# print(var1.readline())
# print(var1.readlines())
for line in var:
    print(line,end="")


