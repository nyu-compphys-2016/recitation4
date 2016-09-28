import math
import numpy as np
import matplotlib.pyplot as plt
import analysis

def f1(x):

    return x*x*np.cos(x)


def f2(x):

    return np.sqrt(x)

analysis.convergence(f1, 0, 4*np.pi, 8*np.pi, 15)
analysis.convergence(f2, 0, 1.0, 2.0/3.0, 15)
analysis.convergence(f2, 0, 3.0, 2.0/3.0, 15)

plt.show()


