# Sine wave animation (without clear ax)
import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.patches as patches


def update(f):
    global tx_step, sin_curve, line1, line2, tx_omega_t, tx_v, ann_v, line3, dot, mode, mode_index, cnt
    k, omega = mode[mode_index]
    # Update items
    # Step
    tx_step.set_text(' Step=' + str(f) + ',k=' + str(k) + ',omega=' + str(omega) + '/step')
    # Sine curve
    sin_curve.set_ydata(np.sin(k * x * math.pi - omega * f))
    # Lines
    line1.set_data([0., - math.cos(- omega * f)], [0., math.sin(- omega * f)])
    line2.set_data([0., - math.cos(- omega * f)], [math.sin(- omega * f), math.sin(- omega * f)])
    # Arrow and text of omega and v
    x_dot = ((omega * f) / math.pi / k) % 6     # Note: math.pi for adjustment x axis as x * pi
    tx_omega_t.set_position((x_dot - 1.2, y_min * 0.8))
    ann_omega_t.set_position((x_dot, - 1.3))
    ann_omega_t.xy = (0., -1.3)
    v = omega / k
    arrow_len = v * 4
    tx_v.set_text('v=omega/k=' + str(f'{v:.2f}'))
    tx_v.set_position((x_dot, 0.1))
    ann_v.set_position((x_dot, 0.))
    ann_v.xy = (x_dot + arrow_len, 0.)
    # line
    line3.set_data([x_dot, x_dot], [0., - 1.4])
    # Dot
    dot.set_center([x_dot, 0.])
    # Change mode (Change k and omega)
    if int(f / 200) % 3 == 1:
        mode_index = 1
    elif int(f / 200) % 3 == 2:
        mode_index = 2
    else:
        mode_index = 0


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
cnt = 0     # Counter to change mode

# Generate figure and axes
fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_xlim(x_min, x_max)
ax.set_ylim(y_min, y_max)
ax.set_title('sin (k*x - omega*t) Note: Step as t')
ax.set_xlabel('x * pi')
ax.set_ylabel('y')
ax.grid()
ax.set_aspect("equal")

# Generate items Note;  The variables of some items need ',' to use set parameters.
tx_step = ax.text(x_min, y_max * 0.8, ' Step=' + str(0) + ',k=' + str(0) + ',omega=' + str(0) + '/step')
x = np.linspace(0, x_max, 100)
y = np.sin(k0 * x * math.pi - omega0 * 0)     # sin(kx - omega*t) Note: math.pi for adjustment x axis as x * pi
sin_curve, = ax.plot(x, y, linestyle='-')
circle = patches.Circle(xy=(0., 0.), radius=1, fill=False)
ax.add_patch(circle)
line1, = ax.plot([0., - math.cos(- omega1 * 0)], [0., math.sin(- omega1 * 0)])
line2, = ax.plot([0., - math.cos(- omega1 * 0)], [math.sin(- omega1 * 0), math.sin(- omega1 * 0)], linestyle=':')
tx_omega_t = ax.text(100., 100., ' - omega*t')
ann_omega_t = ax.annotate(
    '', xy=[0., -1.3], xytext=[0, - 1.3],
    arrowprops=dict(width=1, headwidth=4, headlength=4, facecolor='red', edgecolor='red')
    )
tx_v = ax.text(100., 0.1, 'v=omega/k=' + str(f'{0:.2f}'))
ann_v = ax.annotate(
    '', xy=[0., 0.], xytext=[0., 0.],
    arrowprops=dict(width=1, headwidth=4, headlength=4, facecolor='red', edgecolor='red')
    )
line3, = ax.plot([0., 0.], [0., - 1.4])
dot = patches.Circle(xy=(0, 0.), radius=0.05, color='red')
ax.add_patch(dot)

# Draw animation
anim = animation.FuncAnimation(fig, update, interval=100)
plt.show()
