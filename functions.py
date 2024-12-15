'''Helper functions for cleaner code'''
import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt

def lorenz(x : float,y : float,z : float, dt: float,
           sigma : float, rho : float, beta : float) -> list:
    '''Function to compute a Lorenz attractor function. Given by
        dy/dt = sigma(y-x)
        dy/dt = x(rho-z)-y
        dz/dt = xy-beta*z    
    '''
    dx = sigma * (y - x)
    dy = x * (rho - z) - y
    dz = x * y - beta * z
    return [dt * dx, dt * dy, dt * dz]

def make_attractor_points(x : float,y : float,z : float, dt: float, k: int,
           sigma : float, rho : float, beta : float) -> np.array:
    '''Create array of points of Lorenz system. Where, k = number of iterations'''
    points = [[x,y,z]]
    for _ in range(k):
        lrnz = lorenz(x, y, z, dt, sigma, rho, beta)
        x, y, z = x + lrnz[0], y + lrnz[1], z + lrnz[2]
        points.append([x,y,z])
    return np.array(points).T

# Function to add ticks to a scale
def add_ticks(frame, min_val, max_val, steps, row, column):
    for i, value in enumerate(range(min_val, max_val + 1, steps)):
        tick_label = tk.Label(frame, text=str(value), font=("Arial", 8))
        tick_label.grid(row=row + 1, column=column + i, sticky="n")
