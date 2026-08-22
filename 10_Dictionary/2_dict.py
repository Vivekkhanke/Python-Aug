student = {
    "name" : "Ram",
    "age" : 20
}

# Adding new data
student["city"] = "Pune"
print(student)

# Update existing value
student["age"] = 25
print(student)

# remove data
student.pop("age")
print(student)
# or
# del student["city"]
# print(student)

student.popitem()
print(student)

# clear() -- removes everything
student.clear()
print(student)