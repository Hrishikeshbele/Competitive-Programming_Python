'''
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

Example 1:

Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.
solution idea:
Based on the recursive formula:
f(0) = nums[0]
f(1) = max(num[0], num[1])
f(k) = max( f(k-2) + nums[k], f(k-1) )
'''
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Base Case: nums[0] = nums[0]
        # nums[1] = max(nums[0], nums[1])
        # nums[k] = max(k + nums[k-2], nums[k-1])
        curr,prev=0,0
        for i in nums:
            temp = prev # This represents the nums[i-2]th value
            prev = curr # This represents the nums[i-1]th value
            curr=max(prev,i+temp)
        return curr
