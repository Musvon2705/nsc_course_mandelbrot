import numpy as np
import matplotlib.pyplot as plt
import scipy, numba, pytest, dask, cmath
import time
from utils.benchmark_script import benchmark
from line_profiler import profile

@profile
def mandelbrot_calculation(x: list,
                           y: list,
                           resolution: int = 1024,
                           max_iter: int = 100):
    
    x_grid = np.linspace(x[0], x[1], resolution, endpoint=True)
    y_grid = np.linspace(y[0], y[1], resolution, endpoint=True)

    X, Y = np.meshgrid(x_grid, y_grid)
    C = X + 1j*Y
    Z = np.zeros_like(C)
    N = np.zeros(C.shape, dtype=int)

    for i in range(max_iter):
        mask = np.abs(Z) <= 2
        Z[mask] = Z[mask]*Z[mask] + C[mask]
        N[mask] += 1
    return N


if __name__ == "__main__":
    # Set regions
    x = [-2, 1]
    y = [-1.5, 1.5]

    # Benchmark implementation
    #benchmark(mandelbrot_calculation, x, y, 1024, 100)

    # Create mandelbrot set
    n_grid = mandelbrot_calculation(x, y, 1024, 100)


    # Show mandelbrot set
    #plt.imshow(n_grid)
    #plt.axis('off')
    #plt.show()
