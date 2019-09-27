different ways to calculate ncr in python:

1. import scipy.misc then scipy.misc.comb(N,k)

2. 
import math
def nCr(n,r):
    f = math.factorial
    return f(n) / f(r) / f(n-r)
