'''
This is used for combining two different dictionaries together.
'''
from collections import ChainMap
dic1 = {1:3,2:6}
dic2 = {5:7,9:10}
temp = ChainMap(dic1,dic2)
print(temp)