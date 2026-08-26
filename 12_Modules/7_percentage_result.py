from student import calculate_percentage, check_result 

marks = int(input("Enter your marks : "))

percentage = calculate_percentage(marks, 500)
print("percentage: ", percentage)     
check_result(percentage)