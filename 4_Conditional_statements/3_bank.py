balance = 10000
# withdraw = 1000
withdraw = int(input("Enter the amount you want to withdraw: "))

if balance >= withdraw:
    print("Withdrawal successful. Your your remaining balance is:", balance - withdraw)
else:
    print("Insufficient funds. Your current balance is:", balance)