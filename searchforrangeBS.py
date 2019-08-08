'''
Given a sorted array of integers, find the starting and ending position of a given target value.

Your algorithm’s runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example:

Given [5, 7, 7, 8, 8, 10] and target value 8,

return [3, 4].
'''

class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def searchRange(self, A, B):
        start = -1
        end = -1

        #here we try to find the starting of interval, everytime when A[mid]==target we check if left side also has same num if
        #it has then we decrease the end(e) by 1 
        l = 0
        r = len(A) - 1
        while l <= r:
            mid = (l + r) / 2
            #print mid
            if A[mid] == B and (mid == 0 or A[mid - 1] != B):
                start = mid
                break
            if A[mid] < B:
                l = mid + 1
            #adding 1 in if left elm to mid is also target
            else:
                r = mid - 1
        #here we try to find ending of interval,so when A[mid]==target we check if next elm is also target if so we increase the
        # start(s) by 1 and recalculate mid
        l = 0
        r = len(A) - 1
        while l <= r:
            mid = (l + r) / 2
            if A[mid] == B and (mid == len(A) - 1 or A[mid + 1] != B):
                end = mid
                break
            #adding 1 in if next elm to mid is also target(= sign)
            if A[mid] <= B:
                l = mid + 1
            else:
                r = mid - 1
                
        return [start, end]
                
        


            
                
            
            
        
            
