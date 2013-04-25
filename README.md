HW3-Problem2
============
This computes the sum of the squares of the positive integers up to n, assuming that n is at most 10000.


code in python: timeit("sum_squares(5000)") --> 625 loops, best of 3: 1.65 µs per loop

code in cython: timeit("sum_squares(5000)") --> 625 loops, best of 3: 227 ns per loop

7 times faster!
