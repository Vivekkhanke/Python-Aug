# append() method

cart = ["Laptop", "Mouse"]
cart.append("Keyboard")
print(cart)

# insert() method
# insert(index, value)

fruits = ["apple", "banana"]
fruits.insert(1,"Mango")
print(fruits)

# remove(value) method
fruits = ["apple", "banana", "mango"]
fruits.remove("mango")
print(fruits)

# pop(index)  
fruits = ["apple", "banana", "mango"]
p = fruits.pop(1)
print(p)

for i in fruits:
    print(i)