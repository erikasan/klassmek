import numpy as np, matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

ell = 1
g = 9.81
m = 1

def f(t, y):
    return y[1], ell**2/(2*m**2*np.abs(y[0])**3) - g/2

T = 10

t = np.linspace(0, T, 1000)

result = solve_ivp(f, (0, T), np.array([1, 2]), method='RK45', t_eval=t)

plt.style.use('seaborn-darkgrid')
plt.xlabel(r'$t$', fontsize = 'large')
plt.ylabel(r'$r$',fontsize = 'large')
plt.title(r'$\ell = %.2f, m = %.2f, g = %.2f$' % (ell, m, g), fontsize = 'large')
plt.plot(t, result.y[0])
plt.tight_layout()
plt.show()
