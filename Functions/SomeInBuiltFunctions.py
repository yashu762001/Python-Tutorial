from functools import reduce

# f = lambda n:n+2
# z = f(9)
# print(z)

# f = lambda n:n**2
# z= f(12)
# print(z)

list1 = [1,2,343,55657,57,43,64,2,35,7,9,10,12]

even = list(filter(lambda n:n%2==0,list1))
odd = list(filter(lambda n:n%2!=0,list1))
print(even)
print(id(even))
print(odd)

sum = reduce(lambda a,b:a+b,even)
print(sum)
sum1 = reduce(lambda c,d:c+d,odd)
print(sum1)
hello = list(map(lambda n:n*2,even))
print(hello)
print(even)




