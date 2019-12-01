import numpy as np
import matplotlib.pyplot as plt
from decimal import *


class Dichotomy:

    def __init__(self, a, b, func, epsilon):
        self.a = a
        self.b = b
        self.root = 0
        self.func = func
        self.epsilon = epsilon
        self.table = []

    def find_root(self):
        a = self.a
        b = self.b
        i = 1
        c = 0
        while True:
            c = 0.5 * (a + b)
            fa = self.func(a)
            fb = self.func(b)
            fc = self.func(c)
            self.table += [[i, a, b, c, fa, fb, fc]]
            if fc * fa < 0:
                b = c
            if fc * fb < 0:
                a = c
            i += 1
            print(self.func((a + b) / 2))
            if abs(self.func((a + b) / 2)) < self.epsilon:
                c = 0.5 * (a + b)
                fa = self.func(a)
                fb = self.func(b)
                fc = self.func(c)
                self.table += [[i, a, b, c, fa, fb, fc]]
                self.root = c
                break
        self.table = np.around(self.table, decimals=6)
        self.table = np.array(self.table, dtype=np.float64)

    def draw_graph(self):
        x = np.arange(self.a, self.b, 0.2)
        y = self.func(x)
        plt.plot(x, y)
        plt.grid(True)
        plt.show()

    def draw_table(self):
        table = plt.table(cellText=self.table, loc='center', colLabels=['i', 'a', 'b', 'c', 'f(a)', 'f(b)', 'f(c)'])
        table.auto_set_font_size(False)
        table.set_fontsize(9)
        table.scale(1, 1)
        plt.show()
