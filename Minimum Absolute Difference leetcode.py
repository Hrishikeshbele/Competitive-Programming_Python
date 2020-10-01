'''
Given an array of distinct integers arr, find all pairs of elements with the minimum absolute difference of any two elements. 

Return a list of pairs in ascending order(with respect to pairs), each pair [a, b] follows

a, b are from arr
a < b
b - a equals to the minimum absolute difference of any two elements in arr
 

Example 1:

Input: arr = [4,2,1,3]
Output: [[1,2],[2,3],[3,4]]
Explanation: The minimum absolute difference is 1. List all pairs with a difference equal to 1 in ascending order.

'''

class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        ans=[]
        ## We sort the array because pairs of elements with the minimum absolute difference will definitely 
        ## be next to each other in the sorted array.
        mdiff=float('inf')
        arr=sorted(arr)
        for i in range(len(arr)-1):
            d=arr[i+1]-arr[i]
            if d==mdiff:
                ans.append([arr[i+1],arr[i]][::-1])
            if d<mdiff:
                mdiff=d
                ans=[[arr[i+1],arr[i]][::-1]]
        return ans
