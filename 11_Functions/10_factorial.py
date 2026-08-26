def factorial(n):
    if n == 0 or n == 1:
        return 1
    
    return n * factorial(n-1)  # 4 * 3 * 2 * 1 


fact = factorial(3)
print(fact)
# 3 => 3 * 2 * 1
# 4 => 4 * 3 * 2 * 1