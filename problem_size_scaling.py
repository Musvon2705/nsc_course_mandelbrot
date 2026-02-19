"""
#####################################################
### Lecture 2 - Milestone 4: Problem Size Scaling ###
#####################################################

(This file must be in the same folder as the mandelbrot_numpy_vect.py script)

#############################
### Results from terminal ###
#############################
Resolution: 256
Median: 0.0496s(min = 0.0471, max = 0.0506)
Resolution: 512
Median: 0.2948s(min = 0.2787, max = 0.3148)
Resolution: 1024
Median: 1.3432s(min = 1.3249, max = 1.3625)
Resolution: 2048
Median: 5.4762s(min = 5.4406, max = 5.5061)
Resolution: 4096
Median: 21.7696s(min = 21.7640, max = 22.0643)
"""

from mandelbrot_numpy_vect import mandelbrot_calculation
from utils.benchmark_script import benchmark
import matplotlib.pyplot as plt

# Set regions
x = [-2, 1]
y = [-1.5, 1.5]
max_iterations = 100

print("Resolution: 256")
t_256, result_256 = benchmark(mandelbrot_calculation, x, y, 256, max_iterations)

print("\nResolution: 512")
t_512, result_512 = benchmark(mandelbrot_calculation, x, y, 512, max_iterations)

print("\nResolution: 1024")
t_1024, result_1024 = benchmark(mandelbrot_calculation, x, y, 1024, max_iterations)

print("\nResolution: 2048")
t_2048, result_2048 = benchmark(mandelbrot_calculation, x, y, 2048, max_iterations)

print("\nResolution: 4096")
t_4096, result_4096 = benchmark(mandelbrot_calculation, x, y, 4096, max_iterations)

res_list = [256, 512, 1024, 2048, 4096]
t_list = [t_256, t_512, t_1024, t_2048, t_4096]

plt.plot(res_list, t_list)
plt.xlabel("Resolution")
plt.ylabel("Time")
plt.show()

