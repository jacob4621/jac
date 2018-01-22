def factorial(J):
    if J == 1:
        return 1
    else:
        return (J * factorial(J-1))
print(factorial(10))
