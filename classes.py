def counter():
    a = 0
    def inner():
        nonlocal a
        a += 1
        return a
    return inner
b = counter()
print(b())
print(b())
print(b())
print(b())
