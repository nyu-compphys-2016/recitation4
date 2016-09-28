import numpy as np

def integrate_trapezoid(f, a, b, N):
    # f is a FUNCTION that takes ARRAY input
    h = (b-a) / N
    x = np.linspace(a, b, N+1)
    y = f(x)
    I = h*(0.5*y[0] + 0.5*y[-1] + y[1:-1].sum())

    return I

def integrate_simpson(f, a, b, N):
    # f is a FUNCTION that takes ARRAY input
    if N%2 != 0:
        N -= 1
    h = (b-a) / N
    x = np.linspace(a, b, N+1)
    y = f(x)
    I = h*(y[0] + y[-1]
               + 4*y[1:-1:2].sum()
               + 2*y[2:-2:2].sum())/3.0

    return I

