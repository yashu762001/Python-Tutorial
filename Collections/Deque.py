from collections import deque

array = []
p = deque(array)
p.appendleft(5)
p.appendleft(6)
p.appendleft(7)
# print(p)

# p.pop()
# print(p)

p.popleft()
print(p)

# This is being taught but is not much important.
# The ArrayDeque has inbuilt methods to add and remove elements from first or from last.
# Whereas this is having method similar to a list except that we can add elemnts from left.
