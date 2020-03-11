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
        
