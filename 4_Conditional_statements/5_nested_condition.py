balance = 200000
withdraw = 50000
daily_limit = 100000

if balance >= withdraw:
    if withdraw <= daily_limit:
        print("Withdrawal successful")
    else:
        print("Daily limit exceeded")
else:
    print("Insufficient balance")
        