list = [8,6,4,2,1,10,9,0,88,22,55,47] #1,2,4,6,8,10
n = len(list)

for i in range(n):                   # 0,1 
    for j in range(i+1, n):         # (2, 7) = 2
        if list[i] > list[j]:       # 8 > 6
            list[i], list[j] = list[j], list[i]

print(list)
