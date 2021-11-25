'''
   Numba and PyPy [just-in-time compilers or ahead-of time AOT]
   >> Numba is used to compile small function. Analyse and compiles Python function directly
   to machine code
   >> PyPy is a replacement interpreter that works by analyzing the code at runtime 
   and optimizing the slow loop automatically
'''

# first step with numba
# >> the sum of the square of the array 
from numba import jit
@jit(nopython=True)
def sum_sq(arr : list):
    result = 0
    N = len(arr)
    for i in range(N):
        result += arr[i]
    return result

import numpy as np
from time import time
x = np.random.rand(100000000)
time_1 = time()
sum_sq(x)
time_2 = time()
print(time_2-time_1)