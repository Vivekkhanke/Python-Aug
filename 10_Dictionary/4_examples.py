student = {
    "name" : "Ram",
    "age" : 20
}

for i, j in student.items():
    print(i,j)

for key, value in student.items():
    print(f"key : {key} and Value : {value}")


if "name" in student:
    print("Key exist")
else:
    print("Key doesn't exist")

# print only keys not values
for i in student:
    print(i)