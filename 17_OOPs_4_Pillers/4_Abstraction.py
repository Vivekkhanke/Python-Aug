from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CreditCardPayment(Payment):
    def pay(self, amount):
        print("Paid ", amount, "using credit card.")

class UPIPayment(Payment):
    def pay(self, amount):
        print("Paid ", amount, "using UPI")
        
pay_obj = UPIPayment()
pay_obj.pay(1000)