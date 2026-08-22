student = {
    "name" : "Vivek",
    "marks" : [80,90,85],
    "address" : {
        "city" : "Pune",
        "state" : "Maharashtra"
    }
}

for key in student.keys():
    print(key)
    
print("------------------------------------------")
for val in student.values():
    print(val)
    
print("------------------------------------------")

for key, val in student.items():
    print(key, val)
    
"""
.keys() -- > keys
.values() -- > values
.items() --- > Key + value pairs
"""
