def add_num(*number): #2 --> 10,20
    total = 0          # 30
    
    for num in number:          # num = 10, 20
        total = total + num     # total = 10 + 20
    return total   
        

# result = add_num(10,20)
result = add_num(10,20,30,40)

print(result)