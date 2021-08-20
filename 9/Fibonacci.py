def Fibonacci(n):
    if type(n) not in [int]:
        raise TypeError("Not correct type")
    if n < 0 or n > 30:
        raise ValueError("Number must be less than 30 or greater than -1")
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)