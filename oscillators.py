import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.animation as animation
import seaborn as sns
from scipy.integrate import solve_ivp


l = 1
N = 100
omega = 20
omega2 = omega*omega

x0  = [i*l for i in range(N)]
y0  = [0   for i in range(N)]
vx0 = [0   for i in range(N)]
vy0 = [0   for i in range(N)];

mean   = N/2
var    = 150
y0     = [10*np.exp(-(x0[i] - mean)**2/var) for i in range(N)]
y0[0]  = 0
y0[-1] = 0


def eoms(t, y):
    xdot  = [y[i] for i in range(2*N, 3*N)]
    ydot  = [y[i] for i in range(3*N, 4*N)]
    vxdot = [0] + [omega2*(y[i-1] - 2*y[i] + y[i+1]) for i in range(1, N-1)] + [0]
    vydot = [0] + [omega2*(y[i-1] - 2*y[i] + y[i+1]) for i in range(N+1, 2*N - 1)] + [0]

    return xdot + ydot + vxdot + vydot

T = 10
t = np.linspace(0, T, 300)

result = solve_ivp(eoms, (0, T), y0 = x0 + y0 + vx0 + vy0, t_eval = t)

t = result.t
x = result.y[0:N]
y = result.y[N:2*N]

fig, ax = plt.subplots()
ax.set_xlim(0, (N-1)*l)
ax.set_ylim(-10, 10)
plt.axis('off')
sns.set()
line, = ax.plot(x[:, 0], y[:, 0], '-o', markersize=5, color='deeppink')

def animation_frame(i):
    line.set_xdata(x[:, i])
    line.set_ydata(y[:, i])
    return line,


ani = FuncAnimation(fig, func=animation_frame, frames=t.size, interval=10)
#plt.show()

ani.save('frida.gif', writer='imagemagick', fps=20)
#animation.save('frida.gif', fps=20)
