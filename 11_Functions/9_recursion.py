def countdown(n):
    if n == 3:
        return
    
    print(n)
    countdown(n-1)


countdown(5) # calling the function