def calculate(a,b):   # 10, 5
    add = a + b
    sub = a - b
    mul = a * b
    
    return add, sub, mul # 15, 5, 50
    
result = calculate(10,5)
print(type(result))

a, s, m = calculate(10,5)  # unpacked values

print(a)
print(s)
print(m)

print(type(a))