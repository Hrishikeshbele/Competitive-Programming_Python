'''
Given an array of integers, every element appears twice except for one. Find that single one.
Example :
Input : [1 2 2 3 1]
Output : 3
'''
#solution_1

from collections import Counter
class Solution:
	# @param A : tuple of integers
	# @return an integer
	def singleNumber(self, A):
	    for key,value in Counter(list(A)).items():
            if value == 1:
                return key

#solution_2
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
        #in every iteration will take xor of curr elm with all prev elm in this way if we have repeating elm them their xor will be 
	# zero and only elm whose count is 1 will remain.
        for n in A:
            x = x ^ n   
        return x
#or
#solution_3

def singleNumber(self, A):
	#reduce mape's given function to every elm of iterable.
        return reduce(lambda x,y : x^y, A)

#solution_4

#solution using dict.we increment corresping elm(key) in dict every time we incounter that elm or add to dict if not present and then
# return the key value where value is 1.

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dicn={}
        for i in nums:
            if i not in dicn:
                dicn[i]=1
            else:
                dicn[i]+=1
        for key,val in dicn.items():
            if val==1:
                return key
        
            
        
