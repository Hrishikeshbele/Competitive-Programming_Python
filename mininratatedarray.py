'''
Suppose a sorted array A is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.
'''
def findMin(A):
        left = 0
        right = len(A)-1
        while left < right:
            mid = (left+right)/2
            
            if A[left] < A[right] or A[mid] < A[left]:
                right = mid
            else:
                left = mid+1
        
        return A[left]
