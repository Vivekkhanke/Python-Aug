print("Program started")
a = int(input("Enter a number: "))
b = int(input("Enter another number: "))

try:
    c = a / b
except:
    print("Division by zero is not allowed.")
    
print("Program end")