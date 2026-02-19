"""
Lecture 2 - Milestone 3: Memory Access Patterns
"""

import numpy as np
import time

N = 10000

A = np.random.rand(N, N)

# Row Major Approach
row_start_time = time.perf_counter()
s_row = [np.sum(A[i, :]) for i in range(N)]
row_end_time = time.perf_counter()
print(f"Row major approach time = {row_end_time - row_start_time} seconds")

# Column Major Approach
col_start_time = time.perf_counter()
s_col = [np.sum(A[:, j]) for j in range(N)]
col_end_time = time.perf_counter()
print(f"Column major approach time = {col_end_time - col_start_time} seconds")


A_f = np.asfortranarray(A)

# Row Major Approach with Fortran
row_start_time = time.perf_counter()
s_row = [np.sum(A_f[i, :]) for i in range(N)]
row_end_time = time.perf_counter()
print(f"Row major approach time = {row_end_time - row_start_time} seconds")

# Column Major Approach with Fortran
col_start_time = time.perf_counter()
s_col = [np.sum(A_f[:, j]) for j in range(N)]
col_end_time = time.perf_counter()
print(f"Column major approach time = {col_end_time - col_start_time} seconds")

