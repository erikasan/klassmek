import numpy as np, matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def r(t):
    return np.cosh(t)*np.array([np.cos(t), np.sin(t)])

plt.style.use('seaborn-darkgrid')

fig, ax = plt.subplots()

scale = 10
ax.set_xlim(-scale, scale)
ax.set_ylim(-scale, scale)

ax.axhline(y=0, color='darkgray')
ax.axvline(x=0, color='darkgray')

line, = ax.plot(r(0)[0], r(0)[1], marker = 'o', markersize = 6)

t = np.linspace(0, np.pi, 200)

def animation_frame(i):

    line.set_xdata(r(t[i])[0])
    line.set_ydata(r(t[i])[1])

    return line,

animation = FuncAnimation(fig, func = animation_frame, frames = range(len(t)), interval = 0.0001)

animation.save('oblig.gif', writer='imagemagick', fps=20)
#plt.show()
