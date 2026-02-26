# nsc_course_mandelbrot - Mini Project 1


## Results
| **Implementation** | **Benchmark Time (seconds)** |
| ----------- | ----------- |
| Naive | 10.9860 |
| Numpy | 2.1987 |
| Numba | 0.1263 |

## cProfiler

### Naive Profiling

23009368 function calls in 20.889 seconds

| ncalls | tottime | tottime percall | cumtime | cumtime percall | filename:lineno(function) |
| -------- | ----|--- | ------|---- | ------- |
| 23008310 | 3.264 | 0.000 | 3.264 | 0.000 | {built-in method builtins.abs}|
| 1025 | 0.000 | 0.000 | 0.000 | 0.000 | {built-in method builtins.len}|
|        2 | 0.000 | 0.000 | 0.000 | 0.000 | function_base.py:26(linspace) |
|        2 | 0.000 | 0.000 | 0.000 | 0.000 | {built-in method numpy.zeros} |
|        2 | 0.000 | 0.000 | 0.000 | 0.000 | {built-in method numpy.arange} |
|        2 | 0.000 | 0.000 | 0.000 | 0.000 | {method 'reshape' of 'numpy.ndarray' objects} |
|        2 | 0.000 | 0.000 | 0.000 | 0.000 | numeric.py:1964(isscalar) |
|        2 | 0.000 | 0.000 | 0.000 | 0.000 | {method 'result_type' of 'numpy._core._multiarray_umath._array_converter' objects} |
|        2 | 0.000 | 0.000 | 0.000 | 0.000 | fromnumeric.py:3523(ndim) |
|        2 | 0.000 | 0.000 | 0.000 | 0.000 | {method 'astype' of 'numpy.ndarray' objects} |

#### Analysis of Naive profiling
The number of times ```abs()``` is called does not surprise me. If there are 1024*1024 elements in the c_array, and for each array element, ```abs()``` can be called 100 times (```max_iter```), then ```abs()``` could potentially have been called 104857600 times.
I could limit the amount of calls to ```len()```, by just replacing the use of ```len()``` with the ```resolution```, but the time it takes to call ```len()``` does not seem to use significant amounts of time (see tottime).

* Which function takes most total time?
  * Outside of the mandelbrot function itself, it is the ```abs()``` function which takes longest.
* Are there functions called surprisingly many times?
  * No. See analysis above.
* 


### Numpy Profiling

| ncalls | tottime | percall | cumtime | percall | filename:lineno(function) |
| -------- | ----|--- | ------|---- | ------- |
| 1 | 2.513 | 2.513 | 2.528 | 2.528 | mandelbrot_numpy_vect.py:7(mandelbrot_calculation) |
| 1 | 0.010 | 0.010 | 0.010 | 0.010 | numeric.py:98(zeros_like) |
| 6 | 0.000 | 0.000 | 0.000 | 0.000 | _stride_tricks_impl.py:345(<genexpr>) |
| 4 | 0.000 | 0.000 | 0.000 | 0.000 | {method 'reshape' of 'numpy.ndarray' objects} |
| 4 | 0.000 | 0.000 | 0.000 | 0.000 | {built-in method numpy.array} |
| 3 | 0.000 | 0.000 | 0.004 | 0.001 | _function_base_impl.py:5280(<genexpr>) |
| 2 | 0.004 | 0.002 | 0.004 | 0.002 | {method 'copy' of 'numpy.ndarray' objects} |
| 2 | 0.000 | 0.000 | 0.000 | 0.000 | function_base.py:26(linspace) |
| 2 | 0.000 | 0.000 | 0.000 | 0.000 | _stride_tricks_impl.py:340(_broadcast_to) |
| 2 | 0.000 | 0.000 | 0.000 | 0.000 | {built-in method numpy.zeros} |
| 2 | 0.000 | 0.000 | 0.000 | 0.000 | {built-in method numpy.arange} |
| 2 | 0.000 | 0.000 | 0.000 | 0.000 | _function_base_impl.py:358(iterable) |

#### Analysis of Numpy profiling
Nothing about this profiling surprises me.

* Which function takes most total time?
  * Outside of the mandelbrot function itself, it is the ```np.zero_like()``` function which takes longest.
* Are there functions called surprisingly many times?
  * No.
* How does the NumPy profile compare to naive?
  * It is clear from the profiling that the NumPy implementation is much better - just looking at the amount of function calls, it is much lower overall for the NumPy implementation.



## Line_Profiler

### Naive profile

```
Timer unit: 1e-06 s

Total time: 3.46195 s
File: .\mandelbrot_naive.py
Function: create_complex_grid at line 8

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
     8                                           @profile
     9                                           def create_complex_grid(x: list, y: list, resolution: int = 1024):
    10         1        154.2    154.2      0.0      x_grid = np.linspace(x[0], x[1], resolution, endpoint=True)
    11         1        127.3    127.3      0.0      y_grid = np.linspace(y[0], y[1], resolution, endpoint=True)
    12
    13         1         28.9     28.9      0.0      complex_grid = np.zeros(shape=(resolution, resolution), dtype=complex)
    14      1025        857.7      0.8      0.0      for i in range(len(x_grid)):
    15   1049600     964823.6      0.9     27.9          for j in range(len(y_grid)):
    16   1048576    2495957.3      2.4     72.1              complex_grid[i, j] = complex(x_grid[i], y_grid[j])
    17         1          1.0      1.0      0.0      return complex_grid

Total time: 79.6695 s
File: .\mandelbrot_naive.py
Function: mandelbrot_calculation at line 19

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    19                                           @profile
    20                                           def mandelbrot_calculation(complex_grid: np.ndarray, max_iter: int = 100):
    21         1          3.9      3.9      0.0      grid_size = complex_grid.shape
    22         1         35.0     35.0      0.0      n_grid = np.zeros((grid_size[0], grid_size[1]))
    23      1025        853.1      0.8      0.0      for nx in range(grid_size[0]):
    24   1049600     880098.8      0.8      1.1          for ny in range(grid_size[1]):
    25   1048576     773713.8      0.7      1.0              z = 0
    26   1048576     715429.4      0.7      0.9              n = 0
    27   1048576    1247385.0      1.2      1.6              c = complex_grid[nx, ny]
    28  23008310   31197711.6      1.4     39.2              while abs(z) < 2 and n < max_iter:
    29  21959734   25664591.3      1.2     32.2                  z = z*z + c
    30  21959734   17657944.0      0.8     22.2                  n += 1
    31   1048576    1531756.4      1.5      1.9              n_grid[nx, ny] = n
    32         1          1.5      1.5      0.0      return n_grid
```

* *Which lines dominate runtime? What fraction of total time is spent in the inner loop?*
    * The line including ```abs()``` (line 28) uses the most time. 56.3% of the time is spent in the inner loop (line 29-31).

### NumPy profile

```
Timer unit: 1e-06 s

Total time: 2.19358 s
File: .\mandelbrot_numpy_vect.py
Function: mandelbrot_calculation at line 8

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
     8                                           @profile
     9                                           def mandelbrot_calculation(x: list,
    10                                                                      y: list,
    11                                                                      resolution: int = 1024,
    12                                                                      max_iter: int = 100):
    13
    14         1        149.7    149.7      0.0      x_grid = np.linspace(x[0], x[1], resolution, endpoint=True)
    15         1         61.8     61.8      0.0      y_grid = np.linspace(y[0], y[1], resolution, endpoint=True)
    16
    17         1       3416.1   3416.1      0.2      X, Y = np.meshgrid(x_grid, y_grid)
    18         1      10411.7  10411.7      0.5      C = X + 1j*Y
    19         1       7075.7   7075.7      0.3      Z = np.zeros_like(C)
    20         1         31.9     31.9      0.0      N = np.zeros(C.shape, dtype=int)
    21
    22       101        316.7      3.1      0.0      for i in range(max_iter):
    23       100     872595.3   8726.0     39.8          mask = np.abs(Z) <= 2
    24       100     993442.7   9934.4     45.3          Z[mask] = Z[mask]*Z[mask] + C[mask]
    25       100     306072.8   3060.7     14.0          N[mask] += 1
    26         1          1.6      1.6      0.0      return N
```

* *Which lines dominate runtime? What fraction of total time is spent in the inner loop?*
    * Line 24 uses the most time. The inner loop (line 23-25) uses 99.1% of the time.


## Overall profiling conclusion

* *Based on your profiling results: why is NumPy faster than naive Python?*
  * It is faster because it does not have to potentially iterate 1024*1024*100 times in the inner loop, but instead only have to iterate 100 times.

* *What would you need to change to make the naive version faster? (hint: what does
line profiler tell you about the inner loop?)*
  * It tells me that using ```abs()``` uses a lot of time.

