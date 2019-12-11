
class Chord:

    def __init__(self, a, b, func, epsilon, d1f, d2f):
        self.a = a
        self.b = b
        self.func = func
        self.epsilon = epsilon
        self.d1f = d1f
        self.d2f = d2f
        self.root = 0

    def find_root(self):
        if self.d1f(self.a)*self.d2f(self.a) > 0:
            x0 = self.a
            c = self.b
        else:
            x0 = self.b
            c = self.a
        xp = x0
        while True:
            xn = xp - self.func(xp)*(c-xp)/(self.func(c)-self.func(xp))
            r = xn - xp
            xp = xn
            if abs(r) <= r:
                break
        self.root = xp
