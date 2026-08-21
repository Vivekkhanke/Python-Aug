numbers = {10,20,30}
numbers.add(10)
print(numbers)

# update([value1,value2]) -- adding multiple values

numbers = {10,20}
numbers.update([30,40,50,10])
print(numbers)

a = {1,2,3}
b = {4,5,6,3}
a.update(b)
print(a)

# remove(val) remove simple element
numbers = {10,20,30,40}
numbers.remove(10)
print(numbers)

# difference_update(list) remove multiple elements
numbers = {10,20,30,40}
remove = [20,30]
numbers.difference_update(remove)
print(numbers)

# Error - key error
# numbers = {10,20}
# numbers.remove(100)
# print(numbers)

# if Element exists then remove it but no error
numbers = {10,20}
numbers.discard(200)
print(numbers)

# remove 
numbers = {10,20,30}
x = numbers.pop()
print(x)
print(type(x))

# clear() - remove everything from a set
abc = {10,20,30,40,50}
abc.clear()
print(abc)