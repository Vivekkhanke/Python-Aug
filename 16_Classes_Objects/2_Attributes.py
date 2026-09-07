class Student:
    def details(self, name, age):
        nm = name  # Attributes
        ag = age
        print(nm, " Age: ",ag)
        
obj = Student()   # create an object
obj.details("Vivek", 20)