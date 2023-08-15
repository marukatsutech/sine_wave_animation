# Sine wave animation (without clear ax)(embedded in tkinter)
import math
import numpy as np
from matplotlib.figure import Figure
import matplotlib.animation as animation
import matplotlib.patches as patches
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import tkinter as tk


def change_k(value):
    global k
    k = float(value)


def change_om(value):
    global omega
    omega = float(value)


def switch():
    global on_play
    if on_play:
        on_play = False
    else:
        on_play = True


def update(f):
    global tx_step, sin_curve, line1, line2, tx_omega_t, tx_v, ann_v, line3, dot
    if on_play:
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


# Global variables
x_min = -1.
x_max = 6.
y_min = -1.5
y_max = 1.5

k = 1.
omega = 0.1

on_play = False

# Generate figure and axes
fig = Figure()
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
x = np.linspace(0, x_max, 500)
y = np.sin(k * x * math.pi - omega * 0)     # sin(kx - omega*t) Note: math.pi for adjustment x axis as x * pi
sin_curve, = ax.plot(x, y, linestyle='-')
circle = patches.Circle(xy=(0., 0.), radius=1, fill=False)
ax.add_patch(circle)
line1, = ax.plot([0., - math.cos(- omega * 0)], [0., math.sin(- omega * 0)])
line2, = ax.plot([0., - math.cos(- omega * 0)], [math.sin(- omega * 0), math.sin(- omega * 0)], linestyle=':')
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

root = tk.Tk()
root.title("Sample3")
canvas = FigureCanvasTkAgg(fig, root)
canvas.get_tk_widget().pack(expand=True, fill='both')

toolbar = NavigationToolbar2Tk(canvas, root)
canvas.get_tk_widget().pack()

# Label and spinbox for k1
lbl_k = tk.Label(root, text="k")
lbl_k.pack(side='left')
var_k = tk.StringVar(root)  # variable for spinbox-value
var_k.set(1)  # Initial value
spn_k = tk.Spinbox(
    root, textvariable=var_k, format="%.1f", from_=1, to=10, increment=1,
    command=lambda: change_k(var_k.get()), width=5
    )
spn_k.pack(side='left')

# Label and spinbox for omega
lbl_om = tk.Label(root, text="omega1")
lbl_om.pack(side='left')
var_om = tk.StringVar(root)  # variable for spinbox-value
var_om.set(0.1)  # Initial value
s_om = tk.Spinbox(
    root, textvariable=var_om, format="%.2f", from_=0.1, to=1.0, increment=0.1,
    command=lambda: change_om(var_om.get()), width=5
    )
s_om.pack(side='left')

btn = tk.Button(root, text="Play/Pause", command=switch)
btn.pack(side='left')


# Draw animation
anim = animation.FuncAnimation(fig, update, interval=100)
root.mainloop()
