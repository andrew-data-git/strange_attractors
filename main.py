
from functions import make_attractor_points, add_ticks

import numpy as np
import matplotlib
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
import matplotlib.backends.backend_tkagg as tkagg

# Set-up
root = tk.Tk()
root.wm_title("Lorenz Attractor")
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=5)
root.columnconfigure(2, weight=1)
root.rowconfigure(0, weight=4)
root.rowconfigure(1, weight=0)
root.rowconfigure(2, weight=0)
root.rowconfigure(3, weight=0)
root.rowconfigure(4, weight=0)
root.rowconfigure(5, weight=0)

matplotlib.use('TkAgg')
fig, ax = plt.subplots(figsize=(10,10),subplot_kw=dict(projection='3d'))
canvas = tkagg.FigureCanvasTkAgg(fig, root)
canvas.get_tk_widget().grid(row=0, column=0, columnspan=3, sticky="nsew")

quit_button = ttk.Button(root, text="Quit", command=root.quit)
quit_button.grid(row=4, column=0, columnspan=3)

# Initial conditions
N = 15
n = N+1
colours = plt.cm.magma
init_conditions = {'x':1, 'y':1, 'z':1,
    'dt':0.01, 'sigma':10, 'rho':28, 'beta':8/3,
    'n':n, 'k':1000, 'colours':colours(np.linspace(0, 1, n))
}

# Callback functions

sliders = None
# ax = fig.add_subplot(projection='3d')
# fig.subplots_adjust(bottom=0.25)
def update_fig(val=None):
    # Extract inits
    x_ = init_conditions['x']
    y_ = init_conditions['y']
    z_ = init_conditions['z']
    dt = init_conditions['dt']
    sigma = init_conditions['sigma']
    rho = init_conditions['rho']
    beta = init_conditions['beta']
    n = init_conditions['n']
    k = init_conditions['k']
    colours = init_conditions['colours']

    # Get slider info
    if sliders:
        sigma = sliders['sigma'].get()
        rho = sliders['rho'].get()
        beta = sliders['beta'].get()

    # Plot
    ax.clear()
    for i in range(n):
        points = make_attractor_points(
            x=x_+i, 
            y=y_+i, 
            z=z_+i, 
            dt=dt, 
            k=k, 
            sigma=sigma, 
            rho=rho, 
            beta=beta)
        ax.plot(*points, lw=0.5, c=colours[i])
    ax.set_axis_off()

    # Update logic
    fig.canvas.draw_idle()

def update_s(val=None):
    label_s.config(text=f"{float(val):.3f}")

def update_r(val=None):
    label_r.config(text=f"{float(val):.3f}")

def update_b(val=None):
    label_b.config(text=f"{float(val):.3f}")

def update(val=None):
    update_fig(val)
    if sliders:
        sigma = sliders['sigma'].get()
        rho = sliders['rho'].get()
        beta = sliders['beta'].get()
    else:
        sigma = init_conditions['sigma']
        rho = init_conditions['rho']
        beta = init_conditions['beta']
    update_s(sigma)
    update_r(rho)
    update_b(beta)

# # Window resize
# def on_resize(event):
#     # Get the new window size
#     width = event.width
#     height = event.height
#     fig.set_size_inches(width / fig.dpi, height / fig.dpi)
#     canvas.draw()
# root.bind("<Configure>", on_resize)

# Add labels
tk.ttk.Label(root, text="Sigma").grid(row=2, column=0)
label_s = tk.Label(root, text=f"{float(init_conditions['sigma']):.3f}")
label_s.grid(row=1,column=2)

tk.ttk.Label(root, text="Rho").grid(row=3, column=0)
label_r = tk.Label(root, text=f"{float(init_conditions['rho']):.3f}")
label_r.grid(row=2,column=2)

ttk.Label(root, text="Beta").grid(row=1, column=0)
label_b = tk.Label(root, text=f"{float(init_conditions['beta']):.3f}")
label_b.grid(row=3,column=2)

# Add sliders, with init conditions
smin, smax = 0, 20
slider_s = tk.ttk.Scale(root, from_=smin, to=smax, orient='horizontal', command=update)
slider_s.set(init_conditions['sigma'])
slider_s.grid(row=1, column=1, sticky="ew")

rmin, rmax = 0, 50
slider_r = tk.ttk.Scale(root, from_=rmin, to=rmax, orient='horizontal', command=update)
slider_r.set(init_conditions['rho'])
slider_r.grid(row=2, column=1, sticky="ew")

bmin, bmax = 0, 10
slider_b = tk.ttk.Scale(root, from_=bmin, to=bmax, orient='horizontal', command=update)
slider_b.set(init_conditions['beta'])
slider_b.grid(row=3, column=1, sticky="ew")

sliders = {'sigma':slider_s, 'rho':slider_r, 'beta': slider_b}

# Draw
update_fig()#fig, init_conditions, sliders)
tk.mainloop()