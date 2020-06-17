animals = {"lion","lion","lion","tiger","giraffe","elephant"}
print(animals)
print(len(animals))
print(animals.__contains__("lion"))
# print(animals[2])
# Since there is a random distribution so we can't say that at this particular location this string is gonna come.

print(animals.add("peacock"))
print(animals)
animals.add("hello")
print(animals)
obj = {"lion","tiger","Dog","Cat","Mouse"}
# print(obj)
# animals = animals.intersection(obj)
# print(animals)
animals = animals.union(obj)
print(animals)