class Animal:
    def eat(self):
        print("Animal is eating")
    
class Dog(Animal):
    def bark(self):
        print("Bho bho....")
        
obj = Animal()  # create an object of Animal class
obj.eat()

# obj.bark() error

obj1 = Dog()
obj1.eat()
obj1.bark()