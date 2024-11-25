
from functions import make_attractor_points

import numpy as np
import random
import matplotlib
import tkinter as Tk
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

matplotlib.use('TkAgg')

root = Tk.Tk()
root.wm_title("Embedding in TK")
fig = plt.Figure()
canvas = FigureCanvasTkAgg(fig, root)
canvas.get_tk_widget().pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)

# Initial conditions
x_, y_, z_ = 1, 1, 1
dt = 0.01
sigma=20#10
rho=20#28
beta=8/3
n = 5
k = 1000
colours = plt.cm.magma
colours = colours(np.linspace(0, 1, n))

# Make plot
ax = fig.add_subplot(projection='3d')
fig.subplots_adjust(bottom=0.25)
for i in range(n):
    points = make_attractor_points(x=x_+i, y=y_+i, z=z_+i, dt=dt, k=k, sigma=sigma, rho=rho, beta=beta)
    ax.plot(*points, lw=0.5, c=colours[i])
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
ax.set_title("Lorenz attractor")
ax.set_axis_off()

ax_sigma = fig.add_axes([0.12, 0.2, 0.78, 0.03])
sigma_slider = Slider(ax_sigma, 'sigma', 0, 30, valinit=sigma)
ax_rho = fig.add_axes([0.12, 0.15, 0.78, 0.03])
rho_slider = Slider(ax_rho, 'rho', 0, 30, valinit=rho)
ax_beta = fig.add_axes([0.12, 0.1, 0.78, 0.03])
beta_slider = Slider(ax_beta, 'beta', 0, 30, valinit=beta)

def update(val):
    pos_sigma = sigma_slider.val
    pos_rho = rho_slider.val
    pos_beta = beta_slider.val

    # Update logic
    fig.canvas.draw_idle()

sigma_slider.on_changed(update)
rho_slider.on_changed(update)
beta_slider.on_changed(update)

Tk.mainloop()