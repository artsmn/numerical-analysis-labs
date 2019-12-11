import numpy as np
import sympy as sp
from chmethods import Dichotomy, Chord

epsilon = 0.0001
a = -2
b = 2


def f(x):
    return np.power(x, 5) + 8 * x + 13


dich = Dichotomy(a, b, f, epsilon)
dich.find_root()
print("Root by Dichotomy is {}".format(dich.root))
dich.draw_table()
dich.draw_graph()


x = sp.symbols('x')
d1f = sp.diff(np.power(x, 5) + 8 * x + 13)
d1f = sp.lambdify(x, d1f)
d2f = sp.diff(np.power(x, 5) + 8 * x + 13, x, 2)
d2f = sp.lambdify(x, d2f)


hord = Chord(a, b, f, epsilon, d1f, d2f)
hord.find_root()
print('Root by Chord is {}'.format(hord.root))
