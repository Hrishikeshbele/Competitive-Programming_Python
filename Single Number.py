'''
Given an array of integers, every element appears twice except for one. Find that single one.
Example :
Input : [1 2 2 3 1]
Output : 3
'''
from collections import Counter
class Solution:
	# @param A : tuple of integers
	# @return an integer
	def singleNumber(self, A):
	    for key,value in Counter(list(A)).items():
            if value == 1:
                return key
	    
#solution using xor operator:
'''
#xor operator will work as follow:
res = 7 ^ 3 ^ 5 ^ 4 ^ 5 ^ 3 ^ 4

Since XOR is associative and commutative, above 
expression can be written as:
res = 7 ^ (3 ^ 3) ^ (4 ^ 4) ^ (5 ^ 5)  
    = 7 ^ 0 ^ 0 ^ 0
    = 7 ^ 0
    = 7 
 '''

def singleNumber(self, A):
        x = 0
        
        for n in A:
            x = x ^ n   
        return x
#or
def singleNumber(self, A):
	#reduce mape's given function to every elm of iterable.
        return reduce(lambda x,y : x^y, A)
