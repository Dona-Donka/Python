#!/usr/bin/env python

#Definition of an add method
def add(a, b):
    return a+b

#Definition of a subtract method
def subtract(a, b):
    return a-b

#Definition of a multiply method
def multiply(a, b):
    return a*b

#Definition of a divide method
def divide(a, b):
    return a/b


print """Welcome to the calculator programme!"""
print """Select an operation: 
        1 - add
        2 - subtract
        3 - multiply
        4 - divide"""

operation = input()
print "Set the number: "
a = input()
b = input()

if operation == 1:
    print "%d + %d = %d" % (a, b, add(a, b))
       
elif operation == 2:
    print "%d - %d = %d" % (a, b, subtract(a, b))

elif operation == 3:
    print "%d * %d = %d" % (a, b, multiply(a, b))

elif operation == 4 and 'b' != '0':
    print "%f / %f = %f" % (a, b, divide(a, b))

else:
    print """Please, set the number 1-4 and set number to calculate.
             Remember, that you can't divide by zero!""" 
