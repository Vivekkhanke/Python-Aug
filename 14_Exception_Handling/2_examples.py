# Handle specific exception

# ZeroDivisionError
try:
    a = 10
    b = 0
    c = a / b
except ZeroDivisionError:
    print("Cannot divide by zero.")


# TypeError

a = int(input("Enter a number: "))
b = input("Enter another number: ")

try:
    c = a + b
except TypeError:
    print("Invalid input of b. Please enter a valid number.")
    
print("program end")