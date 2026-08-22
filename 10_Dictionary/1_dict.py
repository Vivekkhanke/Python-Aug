"""
login
username : *****
password : *****
"""

dict = {
    "key1" : "value1",
    "key2" : "value1",
    "key3" : "value1",
}

# empty dictionary
student = {}

student = {
    "name" : "Vivek",
    "age" : 20,
    "course" : "Python",
    "marks" : 85
}

print(student["name"])
# or
# print(student.get("abc")) if key is not available then it will print none
print(student.get("abc", 0))
