#This computes the sum of the squares of the positive integers up to n, assuming that n is at most 10000.
%cython
def sum_squares(long n):
    return n * (n + 1) * (2 * n + 1) / 6
