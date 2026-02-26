import cProfile, pstats

from mandelbrot_naive import mandelbrot_calculation as naive_imp
from mandelbrot_naive import create_complex_grid
from mandelbrot_numpy_vect import mandelbrot_calculation as numpy_imp

x = [-2, 1]
y = [-1.5, 1.5]

cProfile.run('naive_imp(create_complex_grid(x, y, 1024), 100)', 'naive_profile.prof')
cProfile.run('numpy_imp(x, y, 1024, 100)', 'numpy_profile.prof')

for name in ('naive_profile.prof', 'numpy_profile.prof'):
    stats = pstats.Stats(name)
    stats.strip_dirs()
    stats.sort_stats('tottime', 'ncalls', 'cumtime')
    stats.print_stats(10)
