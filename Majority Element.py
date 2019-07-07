'''
Given an array of size n, find the majority element. The majority element is the element that appears more than floor(n/2) times.
'''
#we calculate count for every elm and compare it with len/2

#solution1
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def majorityElement(self, A):
        for x in A:
            if A.count(x)>(len(A)/2):
                return x
#solution2

from collections import Counter
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def majorityElement(self, A):
        lst=dict(Counter(A))
        x = len(A)//2
        return ([i for i in lst if lst[i] > x][0] )
        
