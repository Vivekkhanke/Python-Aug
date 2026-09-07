class Student:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(f"My name is {name} and age {age}")
    
    def display(self):
        print("Name : ",self.name) 
        print("Age : ", self.age) 
           
object = Student("vivek", 30)  # When object is created the constructor called automatically.
object.display()
