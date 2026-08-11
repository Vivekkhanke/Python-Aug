# marks = 75
marks = int(input("Enter your marks : "))
documents = True

if marks > 60 or marks == 60 :
    if documents:
        print("Admission approved")
    else:
        print("Submit required documents")
else:
    print("Admission not eligible")
        