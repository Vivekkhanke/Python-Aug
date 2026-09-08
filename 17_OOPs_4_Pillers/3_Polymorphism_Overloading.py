# CompileTime Polymorphism
# Method/Function Overloading.

class Calculator:
    def add(self, *num):
        return sum(num)


obj = Calculator()
print(obj.add(10,20))
print(obj.add(10,20,30))
print(obj.add(10,20,30,5))