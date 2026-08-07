"""
and
or 
not

"""
age = 22
citizen = True
print(age >= 18 and citizen)

print("-----------------------------------------")
marks = 85
print(marks >= 80 and marks <= 100)
print(marks >= 80 and marks >= 100)
print(marks <= 80 and marks >= 100)
print("-----------------------------------------")

# or operator
print(marks >= 80 or marks >= 100)
print("-----------------------------------------")

# Not operator
print(not (marks < 80))
print(not (marks > 100))
print("-----------------------------------------")

marks = 75
print(not(marks >= 75 or marks >= 100))