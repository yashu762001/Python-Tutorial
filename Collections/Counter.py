# from collections import Counter
#
# a = [1,2,34,5,2,2,2,2,21,1,1,4,5,6]
# c = Counter(a)
# print(c)

# c[4] = 3
# print(c)

# dic = {2:5,4:1}
# c.subtract(dic)
# print(c)

# print(c.most_common())
# arranged in the order they possess values.

# d = {"temple":"run","bug on a":"wire","subway":"suffers","GTA":"San Andreas"}
# e = Counter(d)
# print(e)

# It is useful only when we want to keep record of how many times a element has occurred in the list/set.


def find(list):
    z = 0
    for i in list:
        n=0
        for j in list:
            if(i==j):
                n+=1

        if(n%2!=0):
            z = i
            break


    return z

list = [1,2,10,20,2,1,10,10,20]
print(find(list))





