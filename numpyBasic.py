import numpy as np
import matplotlib.pyplot as plt
from pylab import *
import sympy as sp
from scipy.misc import derivative

# Basic arrays operactions:

a = array([1, 2, 3, 4])
b = array([2, 3, 4, 5])
print(a + b)
print(a * b)
print(a ** b)

x = arange(11)
print("arrange(x) create an array from 0 to x:   ", x)

# y = sin(x)
# print("sin(x) = ", y)

# ploting:
# basic window x,y
x = [1, 2, 3, 4, 5]
y = [10, 25, 20, 25, 50]
fig, ax = plt.subplots()
ax.plot(x, y)
ax.grid()
ax.set(xlabel='variable x', ylabel='variable y',
       title='My first plot!')
# if we can save our plot:
# fig.savefig("firsPlot.png")
plt.show()

# derivative
x = sp.Symbol('x')
print(sp.diff(3 * x ** 2 + 1, x))
fig, ax = plt.subplots()
y = np.linspace(-3, 3)
ax.plot(x, y)
ax.grid()
plt.show()


def f(x):
    return 2 * x ** 3 + 3


print(derivative(f, 2.0))
y = np.linspace(3, -3)
plt.plot(y, f(x))
#plt.plot(y, d(y))
plt.show()
