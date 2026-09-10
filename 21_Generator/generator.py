def numbers():
    yield 10
    yield 20
    yield 30
    return 50

num = numbers()
print(num)

print(next(num))
print(next(num))
print(next(num))