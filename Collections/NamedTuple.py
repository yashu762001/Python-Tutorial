from collections import namedtuple

# a = namedtuple('courses', 'name,technology')
# s = a('data science','python')
# print(a)
# print(s)

# It is similar to a dictionary but with a name and also immutable just like the string and tuple.

info = namedtuple("human","name ,age ,height, color")
p = info(name="yash",age=19,height=165,color="Fair")
# print(p.color)
# print(len(p))
# print(p.name)
p= dict(p._asdict())
p['name']= "yashu"
print(p)
# len method tells the total number of keys present.

# The name of above dictionary is human with several keys:name,age,height,color.
# corresponding to name we have certain value,similarly corresponding to every field there is certain value.
# Now we want value corresponding to the key. So we will use object reference.the key.
# Only use is that it means list a bit systematic.
# To convert namedtuple to a regular dictionary, one thing can be thing.

info = namedtuple('human','name age height color')
p = info._make(["yash",19,165,"Fair"])
print(p)
print(p.age)
print(p.name)

#  NamedTuple is a Tuple so once the values are assigned to different fields they can't be updated.