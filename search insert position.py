'''
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Example 1:

Input: [1,3,5,6], 5
Output: 2
solution idea: we do iterative binary search until left>right or left or right move outside array.we return left which would be new index of inserted elm.
'''

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left=0
        right=len(nums)
        while left<=right and left<len(nums) and right>=0:
            mid=(left+right)//2
            if target==nums[mid]:
                return mid
            if target<nums[mid]:
                right=mid-1
            else:
                left=mid+1
        return left
        
