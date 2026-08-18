list1 = [1,3,5,4]
list2 = [2,4,3,1]
list3 = [4,2,3,4]

result = [8,9,2,4,7,3]

for i in list1:
    for j in list2:
        for k in list3:
            if i+j+k in result:
                print(f"{i} + {j} + {k} = {i+j+k}")