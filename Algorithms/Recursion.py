from math import *


### RECURSION ###

def factorial(x):
    if x == 0:
        return 1
    else:
        return x * factorial(x - 1)


print "5! = ", factorial(5)


def power(x, y):
    if y == 0:
        return 1
    else:
        return x * power(x, y - 1)


# The function above is performed (x multiply by x) y-times
print "2^3 = ", power(2, 3)


def fib(x):
    if x < 2:
        return x
    else:
        return fib(x - 1) + fib(x - 2)


# 0 + 1 + 1 + 2 + 3 + 5 + 8 + ...
print "fib(8): ", fib(8)


def euclid(m, n):
    while m % n != 0:
        if m > n:
            return euclid(m - n, n)
        else:
            return euclid(m, n - m)
    return n


print "euclid(1989, 867): ",  euclid(1989, 867)
