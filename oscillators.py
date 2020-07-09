import numpy as np, matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

l = 1
N = 2
k = 9
m = 5

x0  = [i*l for i in range(N+1)]
y0  = [0   for i in range(N+1)]
vx0 = [0   for i in range(N+1)]
vy0 = [0   for i in range(N+1)]; vy0[int(N/2)] = 13

def eoms(t, y):
    xdot  = [y[i] for i in range(2*(N+1), 3*(N+1))]
    ydot  = [y[i] for i in range(3*(N+1), 4*(N+1))]
    vxdot = [0] + [-k/m*(2*y[i] - y[i-1] - y[i+1]) for i in range(1, N)] + [0]
    vydot = [0] + [-k/m*(2*y[i] - y[i-1] - y[i+1]) for i in range(N+2, 2*(N+1) - 1)] + [0]

    xdot  = tuple(xdot)
    ydot  = tuple(ydot)
    vxdot = tuple(vxdot)
    vydot = tuple(vydot)

    return xdot + ydot + vxdot + vydot

T = 10
t = np.linspace(0, T, 10000)

result = solve_ivp(eoms, (0, T), y0 = x0 + y0 + vx0 + vy0, t_eval = t)
x  = result.y[0:N+1]
y  = result.y[N+1:2*(N+1)]
vx = result.y[2*(N+1): 3*(N+1)]
vy = result.y[3*(N+1): 4*(N+1)]

plt.style.use('seaborn-darkgrid')
plt.plot(t, y[1])
plt.show()
