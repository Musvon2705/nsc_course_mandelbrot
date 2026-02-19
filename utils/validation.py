from mandelbrot_naive import mandelbrot_calculation as naive
from mandelbrot_naive import create_complex_grid as naive_helper_func
from mandelbrot_numpy_vect import mandelbrot_calculation as numpy_impl
import numpy as np

x = [-2, 1]
y = [-1.5, 1.5]
resolution = 1024
max_iterations = 100

naive_results = naive(naive_helper_func(x, y, resolution), max_iterations)

numpy_results = numpy_impl(x, y, resolution, max_iterations)

if np.allclose(naive_results, numpy_results):
    print("Results match!")
else:
    print("Results differ!")
    diff = np.abs(naive_results - numpy_results)
    print(f"Max difference: {diff.max()}")
    print(f"Different pixels: {(diff > 0).sum()}")