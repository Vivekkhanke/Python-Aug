try:
    file = open(r"D:\Python Aug\15_File_Handling\student.txt", "r")
    data = file.read()
    print(data)
    
    line = file.readline()
    print(line)
    
    line = file.readlines()
    print(line)
    
    file.close()
except:
    print("File not found, please check the path again.")
