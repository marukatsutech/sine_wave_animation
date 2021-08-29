# Sine wave animation
import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.patches as patches


def update(f):
    ax.cla()  # Clear ax
    set_axis()

    global mode, mode_index, x0, cnt
    k, omega = mode[mode_index]
    ax.text(x_min, y_max * 0.8, ' Step=' + str(f) + ',k=' + str(k) + ',omega=' + str(omega) + '/step')
    # Draw sin curve
    y = np.sin(k * x * math.pi - omega * f)     # sin(kx - omega*t) Note: math.pi for adjustment x axis as x * pi
    ax.plot(x, y, linestyle='-')
    # Draw circle and lines
    circle = patches.Circle(xy=(0., 0.), radius=1, fill=False)
    ax.add_patch(circle)
    ax.plot([0., - math.cos(- omega * f)], [0., math.sin(- omega * f)])
    ax.plot([0., - math.cos(- omega * f)], [math.sin(- omega * f), math.sin(- omega * f)], linestyle=':')
    # dot position
    x_dot = ((omega * f) / math.pi / k) % 6     # Note: math.pi for adjustment x axis as x * pi
    # Draw translation as step(time)
    ax.text(x_dot - 1.2, y_min * 0.8, ' - omega*t')
    ax.annotate('', xy=[0., -1.3], xytext=[x_dot, - 1.3], arrowprops=dict(width=1, headwidth=4, headlength=4, facecolor='red', edgecolor='red'))
    # Draw Phase velocity
    v = omega / k
    arrow_len = v * 4
    ax.text(x_dot, 0.1, 'v=omega/k=' + str(f'{v:.2f}'))
    ax.annotate('', xy=[x_dot + arrow_len, 0.], xytext=[x_dot, 0.], arrowprops=dict(width=1, headwidth=4, headlength=4, facecolor='red', edgecolor='red'))
    ax.plot([x_dot, x_dot], [0., - 1.4])
    # Draw dot
    dot = patches.Circle(xy=(x_dot, 0.), radius=0.05, color='red')
    ax.add_patch(dot)
    # Change mode (Change k and omega)
    if int(f / 200) % 3 == 1:
        mode_index = 1
    elif int(f / 200) % 3 == 2:
        mode_index = 2
    else:
        mode_index = 0


def set_axis():
    ax.set_xlim(x_min, x_max)
    ax.set_ylim(y_min, y_max)
    ax.set_title('sin (k*x - omega*t) Note: Step as t')
    ax.set_xlabel('x * pi')
    ax.set_ylabel('y')
    ax.grid()
    ax.set_aspect("equal")


# Global variables
x_min = -1.
x_max = 6.
y_min = -1.5
y_max = 1.5

k0 = 1.
k1 = 2.
omega0 = 0.1
omega1 = 0.2
mode_index = 0
mode = [[k0, omega0], [k1, omega0], [k0, omega1]]   # combination of k and omega

x = np.linspace(0, x_max, 100)

x0 = 0.
cnt = 0

# Generate figure and axes
fig = plt.figure()
ax = fig.add_subplot(111)

# Draw animation
set_axis()
anim = animation.FuncAnimation(fig, update, interval=100)
plt.show()
