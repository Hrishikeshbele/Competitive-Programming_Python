'''
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

'''

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        l,r=0,len(nums)-1
        ans=[-1,-1]
        # corner cases 
        if not nums:
            return ans
        if len(nums)<2 and nums[0]!=target:
            return ans
        if len(nums)<2 and nums[0]==target:
            return [0,0]
        
        
        while l<=r:
            mid=(l+r)//2
            if nums[mid]==target:
                ans=[mid,mid]
                if nums[mid-1]==target:
                    j=mid-1
                    while nums[j]==target and j >=0:
                        ans[0]=j
                        j-=1
                        
                if mid+1<len(nums) and nums[mid+1]==target:
                    
                    if nums[mid+1]==target:
                        k=mid+1
                        while   k<len(nums) and nums[k]==target:
                            ans[1]=k
                            k+=1
                            
            if nums[mid]<target:
                l=mid+1
            else:
                r=mid-1
        return ans
                
        
