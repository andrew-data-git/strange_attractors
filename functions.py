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

if __name__ == '__main__':

    # Initial conditions
    x_, y_, z_ = 1, 1, 1
    dt = 0.01
    sigma=10
    rho=28
    beta=8/3
    n = 5
    k = 10000
    colours = plt.cm.magma
    colours = colours(np.linspace(0, 1, n))

    # Make plot
    ax = plt.figure().add_subplot(projection='3d')
    for i in range(n):
        points = make_attractor_points(x=x_+i, y=y_+i, z=z_+i, dt=dt, k=k, sigma=sigma, rho=rho, beta=beta)
        ax.plot(*points, lw=0.5, c=colours[i])
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")
    ax.set_title("Lorenz attractor")
    ax.set_axis_off()

    plt.show()