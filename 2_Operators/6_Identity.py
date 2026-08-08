"""
is          -- same object
is not      -- not the same object
"""
a = [1,2,3]
b = a
c = [1,2,3]

print(a is b)
print(a is c)

print("---------------------------------")

a = [1,2]
b = [1,2]

print(a is b)
print(a == b)