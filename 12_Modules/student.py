def calculate_percentage(marks, total):
    return (marks / total) * 100

def check_result(percentage):
    if percentage >= 35:
        print("Pass")
    else:
        print("Fail")

