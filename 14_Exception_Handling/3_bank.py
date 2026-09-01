balance = 10000
try:
    amount = int(input("Enter withdrawal amount : "))
    balance = balance - amount
except:
    print("Please enter valid number..")
finally:
    print("Hello") 
print("program ends")