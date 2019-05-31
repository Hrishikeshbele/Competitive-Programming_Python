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
	    
