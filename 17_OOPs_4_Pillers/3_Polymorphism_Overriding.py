# Method Overriding

class Animal:
    def sound(self):
        print("Animal makes a sound..")
    
class Dog(Animal):
    def sound(self): # type: ignore
        return "Dog barks.."

obj = Dog()
print(obj.sound())