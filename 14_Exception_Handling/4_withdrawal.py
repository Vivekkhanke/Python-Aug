balance = 10000

try:
    amount = float(input("Enter the amount to withdraw: "))
    if amount <= 0:
        raise ValueError("Amount must be greater than zero")
    if amount > balance:
        raise ValueError("Insufficient balance")
    balance = balance - amount   # balance -= amount
except ValueError:
    print("Transaction failed : ",ValueError)

else:
    print("Withdrawal successful...")
    print("remaining balance : ", balance)
    
finally:
    print("processing...")