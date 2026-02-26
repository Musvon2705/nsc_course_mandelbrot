import numpy as np
import matplotlib.pyplot as plt
from numba import njit, prange
import time
from utils.benchmark_script import benchmark

@njit
def mandelbrot_calculation(x: list,
                           y: list,
                           resolution: int = 1024,
                           max_iter: int = 100):
    x_grid = np.linspace(x[0], x[1], resolution)
    y_grid = np.linspace(y[0], y[1], resolution)
    result = np.zeros((resolution, resolution), dtype=np.int32)

    for ny in range(resolution):
        for nx in range(resolution):
            z = 0
            n = 0
            c = x_grid[nx] + 1j * y_grid[ny]
            while z.real*z.real + z.imag*z.imag <= 4 and n < max_iter:
                z = z*z + c
                n += 1
            result[nx, ny] = n
    return result



if __name__ == "__main__":
    # Set regions
    x = [-2, 1]
    y = [-1.5, 1.5]

    # Create mandelbrot set from complex grid + warm-up
    n_grid = mandelbrot_calculation(x, y, 1024, 100)

    benchmark(mandelbrot_calculation, x, y, 1024, 100)


    # Show mandelbrot set
    plt.imshow(n_grid)
    plt.axis('off')
    plt.show()
