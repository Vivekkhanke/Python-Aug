l1 = [2,4,1,5,3,7,6,3,3]
equal = 6
n = len(l1)
# pair 2,4  5,1  

for i in range(n):              # 0 
    for j in range(i+1, n):     # 1, 6 = 1
        if l1[i] + l1[j] == equal: #2+4 == 6
            print(f"Pair found {l1[i], l1[j]}") 
            
             


