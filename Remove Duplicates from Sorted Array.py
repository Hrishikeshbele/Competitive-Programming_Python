'''
Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Example 1:

Given nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.

solution idea: maintain a pointer to next index to be filled with a new number. check every number of list against prev num and if diff, fill it
at pointer and move the pointer to next place.
'''
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        point=0
        for i in range(len(nums)):
            if i==0 or nums[i]!=nums[i-1]:
                nums[point]=nums[i]
                point+=1

        return point
        
        
 ### solution 2 (2 pointers)
 # idea is use 2 pointers , one pointing to 1st elm of duplicate nums series and other to iterate over next elms. while iterating if we found elm not equal to elm at 1st pointer
 # i.e 1st elm of duplicate series we point our 1st pointer to 2nd pointer and iterate again with help of second pointer and each time we find new elm we add it to list .

class Solution:
    # @param A : list of integers
    # @return an integer
    def removeDuplicates(self, A):
        i,j=0,0
        num=1
        while i<len(A) and j<len(A):
            if A[i]==A[j]:
                j+=1
            elif A[i]!=A[j]:
                A[num]=A[j]
                i=j
                num+=1
        return(num)
            
