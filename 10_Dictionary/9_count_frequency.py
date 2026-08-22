number = [1,2,2,3,3,3,4,4]
count = {}

for num in number:
    count[num] = count.get(num, 0) + 1   

print(count)

# 1 --> 