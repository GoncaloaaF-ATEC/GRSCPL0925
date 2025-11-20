def func1():
    return "valor1", "valor2"


def func2():
    return "valor55", "valor66"



print(func1())

v1, v2 = func1()

print(v1, v2)


v1, _ = func2()

print(v1, v2)
