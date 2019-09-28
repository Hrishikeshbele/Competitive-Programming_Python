'''
finding gcd given set of number.
'''

1.
def computeHCF(x, y):

   # This function implements the Euclidian algorithm to find H.C.F. of two numbers
   while(y):
       x, y = y, x % y
   return x
2. 
def gcd_recursive(a, b):
    if b == 0:
        return a
    else:
        return gcd_recursive(b, a % b)
3.
gcd = lambda m,n: m if not n else gcd(n,m%n)

4.
 from fractions import gcd
 gcd(20,8)
 >> 4
 
 5. GCD of group of elm(list):
 
from fractions import gcd
from functools import reduce
def find_gcd(list):
    x = reduce(gcd, list)
    return x
 
