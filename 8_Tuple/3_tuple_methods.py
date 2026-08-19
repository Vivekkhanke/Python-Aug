# count(value)
num = (10,20,10,30,10,40)
c = num.count(10)
print(f"The count of value 10 is : {c} times")

# index(value) 
ind = num.index(30)
print(ind)

# len() calculate total numbers of values in tuple

total_num = len(num)
print(total_num)

# max(val) -- largest value in tuple
largest = max(num) 
print(largest)

# min(val) -- largest value in tuple
lowest = min(num) 
print(lowest)

# sort(tuple) sort a value -- sorted function returns list not a tuple
sort = tuple(sorted(num))
print(sort)
desc = tuple(sorted(num, reverse= True))  # descending order
print(desc)
