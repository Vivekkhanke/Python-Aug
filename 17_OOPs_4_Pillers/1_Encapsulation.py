class BankAccount:
    
    def __init__(self, balance):
        self.balance = balance
        
    def deposit(self, amount):
        self.balance += amount # self.balance = balance + amount
    
    def get_balance(self):
        return self.balance   
    
obj = BankAccount(100)
obj.deposit(50)
result = obj.get_balance()
print(result)