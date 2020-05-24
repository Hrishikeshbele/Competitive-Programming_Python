'''
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note: The solution set must not contain duplicate triplets.

Example:
Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]

idea: first we sort the array then we iterate throught list with 2 pointers.we set target as (0-curr elm) and use 2 pointers to find if 
there is any pair in list whose sum is equal to target in same way as 2 sum problem. if we find such pair we add it to ans. 
'''

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        ans=set()
        for i in range(len(nums)-2):
            part_tar=-nums[i]
            start=i+1
            end=len(nums)-1
            while start<end:
                part_sum=nums[start]+nums[end]
                if part_sum==part_tar:
                    ans.add((nums[i],nums[start],nums[end]))
                    end-=1
                    start+=1
                elif part_sum>part_tar:
                    end-=1
                else:
                    start+=1
                    
        return (ans)
