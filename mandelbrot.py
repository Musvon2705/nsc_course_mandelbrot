import numpy as np
import matplotlib.pyplot as plt
import scipy, numba, pytest, dask, cmath
import time

def create_complex_grid(x: list, y: list, resolution: int = 1024):
    x_grid = np.linspace(x[0], x[1], resolution, endpoint=True)
    y_grid = np.linspace(y[0], y[1], resolution, endpoint=True)

    complex_grid = np.zeros(shape=(resolution, resolution), dtype=complex)
    for i in range(len(x_grid)):
        for j in range(len(y_grid)):
            complex_grid[i, j] = complex(x_grid[i], y_grid[j])
    return complex_grid

def mandelbrot_calculation(complex_grid: np.ndarray, max_iter: int = 100):
    grid_size = complex_grid.shape
    n_grid = np.zeros((grid_size[0], grid_size[1]))
    for nx in range(grid_size[0]):
        for ny in range(grid_size[1]):
            z = 0
            n = 0
            c = complex_grid[nx, ny]
            while abs(z) < 2 and n < max_iter:
                z = z*z + c
                n += 1
            n_grid[nx, ny] = n
    return n_grid

# Set regions
x = [-2, 1]
y = [-1.5, 1.5]
 
start_time = time.time()

# Create complex number grid
grid = create_complex_grid(x, y, 4096)

# Create mandelbrot set from complex grid
n_grid = mandelbrot_calculation(grid, 100)

end_time = time.time()

# Naive implementation time: 4.5468645095825195 seconds (for 1024 resolution and 100 as max iterations)
print(f"Naive implementation time: {end_time-start_time} seconds")

# Show mandelbrot set
plt.imshow(n_grid)
plt.axis('off')
plt.show()
