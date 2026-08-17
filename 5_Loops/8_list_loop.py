a = [1,2,3,4,5]   # 5 
b = [2,1,4,3,5]   # 2
c = [7,4,5,1,2]   # 1

result = [10,2,8,9]

for i in a:
    for j in b:
        for k in c:
            total = i+j+k
            
            if total in result:
                print(i,j,k, "= ", total)