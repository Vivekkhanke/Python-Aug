# Type Casting in Python
# int()
# float()
# str()
# bool()

num = int("100")
print(num)
print(type(num))

price = float('99.99')
print(price)
print(type(price))

age = 25
text = str(age)
print(text)
print(type(text))

# bool()
a = 1
b = 0
c = bool(a)
d = bool(b)
print(c)
print(d)

# Type casting error
age = "one"
int_age = int(age)  
print(int_age)  # This will raise a ValueError because "one" cannot be converted to an integer

