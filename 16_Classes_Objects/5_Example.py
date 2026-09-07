class Customer:
    
    def  __init__(self, name, email, balance):
        self.name = name
        self.email = email
        self.balance = balance
    
    def display_customer(self):
        print("Name : ", self.name)
        print("Email : ", self.email)
        print("Balance : ", self.balance)
    
    def deposit(self, amount):
        self.balance += amount     # balance = balance +  amount
        print("Amount deposited : ", amount)
        
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount  # balance = balance - amount
            print("Amount withdrawn : ", amount)
            print("Your current balance is : ", self.balance)
        else:
            print("Insufficient balance")
            
obj = Customer("Vivek","Vivek@gmail.com", 100)
obj.display_customer()
# obj.deposit(5000)
obj.withdraw(50)