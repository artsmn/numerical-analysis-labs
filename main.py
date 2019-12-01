import numpy as np
from chmethods import Dichotomy

epsilon = 0.0001
function = lambda x: np.power(x, 5) + 8 * x + 13

dich = Dichotomy(-2, 2, function, epsilon)
dich.find_root()
print("Root is {}".format(dich.root))
dich.draw_table()
dich.draw_graph()

