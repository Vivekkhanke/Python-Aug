def add_num(*number): #2 --> 10,20
    total = 0          # 30
    
    for num in number:          # num = 10, 20
        total = total + num     # total = 10 + 20
    return total   
        
a = int(input("Enter a value of a : "))
b = int(input("Enter a value of b : "))
c = int(input("Enter a value of c : "))

p = add_num(a,b,c)
print(f"Addition of {a} + {b} + {c} = {p}")