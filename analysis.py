import numpy as np
import matplotlib.pyplot as plt
import integrate as my_int

def convergence(f, a, b, exact, num):
    N = np.power(2, np.arange(1,num+1))

    I_trap = np.empty(num)
    I_simp = np.empty(num)

    for i in range(num):
        I_trap[i] = my_int.integrate_trapezoid(f, a, b, N[i])
        I_simp[i] = my_int.integrate_simpson(f, a, b, N[i])


    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    ax.plot(N, np.fabs(I_trap-exact), 'r+', ms=20, mew=2)
    ax.plot(N, np.fabs(I_simp-exact), 'b+', ms=20, mew=2)

    ax.set_xscale('log')
    ax.set_yscale('log')



