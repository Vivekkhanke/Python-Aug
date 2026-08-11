performance = 82
salary = 50000

if performance >= 90:
    bonus = salary * 0.20   # 20 % bonus
elif performance >= 75:
    bonus = salary * 0.15
elif performance >= 60:
    bonus = salary * 10
else:
    bonus = 0

salary = salary + bonus
print(f"Your Bonus is := {bonus} and now your current salary is {salary} ")

print(type(salary))