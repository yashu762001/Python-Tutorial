animals = (10,123,35,'lion','tiger','elephant','lion')
print(id(animals))
# print(animals)
# print(animals.count("lion"))
# print(animals.index("lion"))
# print(animals)
# print(animals[1])
#  This is immutable so if any change is to be done then a new list of items is forced within the memory just
#  like the string.

animals = list(animals)
print(id(animals))
animals[2] = 45
animals = tuple(animals)
print(animals)
print(id(animals))

#  So to update a tuple first convert it into a list , then list can be updated very easily and then convert list
# back to tuple.