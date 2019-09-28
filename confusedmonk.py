'''
The Monk wants to teach all its disciples a lesson about patience, since they are always in a hurry to do something crazy. To teach them this, he gives them a list of N numbers, which may or may not be distinct. The students are supposed to solve a simple Mathematical equation based on the array of these N numbers.

g(x) - GCD (a[ 0 ], a[ 1 ], a[ 2 ]... a[n-1] )
f(x) - (a[ 0 ] * a[ 1 ] * a[ 2 ]... * a[n-1] )
The value of the MonkQuotient is: 109 + 7.

The equation to be solved is: ( f(x)g(x) ) % MonkQuotie
SAMPLE INPUT:
2
2 6
SAMPLE OUTPUT 
144
Explanation:Here we can see that the product of the elements of array is 12 and the GCD of the array comes out to be 2 . 
Thus the answer would be 12^2 which is 144.
'''

n=int(input())
arr=[int(x) for x in input().split()]
from fractions import gcd
from functools import reduce
def find_gcd(list):
    x = reduce(gcd, list)
    return x
def multiplyList(myList) : 
    # Multiply elements one by one 
    result = 1
    for x in myList: 
         result = result * x  
    return result  

print((multiplyList(arr)**find_gcd(arr))%(10**9 + 7))
