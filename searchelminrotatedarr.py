'''
Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7  might become 4 5 6 7 0 1 2 ).

You are given a target value to search. If found in the array, return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Input : [4 5 6 7 0 1 2] and target = 4
Output : 0

'''
'''
the main idea is that we need to find some parts of array that we could adopt binary search on that, which means we need to find some completed sorted parts, 
then determine whether target is in left part or right part.There is at least one segment (left part or right part) is monotonically increasing.
If the entire left part is monotonically increasing, which means the pivot point is on the right part
  If left <= target < mid ------> drop the right half
  Else ------> drop the left half
If the entire right part is monotonically increasing, which means the pivot point is on the left part
  If mid < target <= right ------> drop the left half
  Else ------> drop the right half
'''
  
#solution 1
  class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l,r=0,len(nums)-1
        #we use = because finally l and r become same as index of tar elm
        while(l<=r):
            mid=(l+r)//2
            if target==nums[mid]:
                return mid
            #if nums[mid]>= num[l] it mean that first half is in sorted order
            #then again we check if tar elm is l and mid if yes we search in first
            #half o.w we search in second half similarly for second half 
            if nums[l]<=nums[mid] :
                if nums[l]<=target<=nums[mid]:
                    r=mid-1
                else:
                    l=mid+1
                    
            else:
                if nums[mid]<=target<=nums[r]:
                    l=mid+1
                else:
                    r=mid-1
         
        return -1
 ##solution 2
 
 #here idea is first find the min elm in list and then do normal binary search on left and right part of
 #min elm as both parts will be sorted
 def searchInsert( A, B):
    s=0
    j=0
    e=len(A)-1
    while(s<=e):
        mid=(s+e)//2
        if A[mid]==B:
            return mid
        elif A[mid]<B:
            s=mid+1
        elif A[mid]>B:
            e=mid-1
    return -1

class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def search(self, A, B):
        x=A.index(min(A))
        list(A)
        searchInsert(A[:x],B)
        searchInsert(A[x:],B)
        
        
