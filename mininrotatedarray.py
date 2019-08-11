'''
Suppose a sorted array A is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.
'''
'''
ans: if we observe the rotated array we can see that since we use round up for mid, and left < right , right would never be the same as mid
      Therefore, we compare mid with right, since they will never be the same from.if nums[mid] < nums[right] we see that second half(arr[mid:])
      is in sorted order and min lies in first half similarly if nums[mid]>nums[right] we can see that min lies in first half arr[:mid+1] is sorted 
      and min lies in second half so we set l to mid+1 and when we end while loop l=r=min elm
  '''
def findMin(A):
        l,r=0,len(arr)-1
        while l<r:
            mid=(l+r)//2
            if arr[mid]>arr[r]:
                l=mid+1    
            else:
                r=mid
                
        return arr[l]
