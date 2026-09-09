from abc import ABC, abstractmethod

class Notification(ABC):
    @abstractmethod
    def send(self, message):
        pass

class EmailNotification(Notification):
    def send(self, message):
        print("Sending email : ", message)

class WhatsappNotification(Notification):
    def send(self, message):
            print("Sending whatsapp : ", message)

obj = EmailNotification()
obj.send("Hello.........")