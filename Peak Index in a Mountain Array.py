'''
Let's call an array arr a mountain if the following properties hold:

arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... arr[i-1] < arr[i]
arr[i] > arr[i+1] > ... > arr[arr.length - 1]
Given an integer array arr that is guaranteed to be a mountain, return any i such that arr[0] < arr[1] < ... arr[i - 1] < arr[i] > arr[i + 1] > ... > arr[arr.length - 1].

 

Example 1:

Input: arr = [0,1,0]
Output: 1

idea: If the midpoint is greater than the previous number AND if the midpoint's greater than the next number we found the peak. and for nevigating the left right we comparate 
mid element with previous elm and next elm if mid element is less than prev elm means it is increasing sequence so mointain peak must be on right side so we search in right side 
and vice-versa.
'''

class Solution(object):
    def peakIndexInMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        l,r=0,len(arr)-1
        
        while l<=r:
            mid=(l+r)//2
            if arr[mid-1]<arr[mid]>arr[mid+1]:#found the mountain
                return mid
            elif arr[mid]<arr[mid-1]:#if sequence is decreasing then mointain must be on left
                r=mid-1
            elif arr[mid]<arr[mid+1]:#if sequence is increasing then mointain must be on right
                l=mid+1
        
                
        
