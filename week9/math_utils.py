import math


def square_root(a):
    if type(a) not in [int, float] or a < 0:
        return "invalid input"
    return math.sqrt(a)


def power(a, b):
    if type(a) not in [int, float] or type(b) not in [int, float]:
        return "invalid input"
    return math.pow(a, b)


def fact(n):
    if type(n) != int or n <= 0:
        return "invalid input"

    nFactorial = 1
    for i in range(1, n + 1):
        nFactorial *= i
    return nFactorial
