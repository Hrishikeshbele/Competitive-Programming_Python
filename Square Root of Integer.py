'''
Implement int sqrt(int x).

Compute and return the square root of x.
'''
class Solution:
    # @param A : integer
    # @return an integer
    def sqrt(self, A):
        s=1
        e=A
        while s<=e:
            mid=(s+e)/2
            # Checking if mid = floor(sqrt(A))
            if mid*mid<=A and (mid+1)*(mid+1)>A:
                return mid
            elif mid*mid>A:
                e=mid-1
            elif mid*mid<A:
                s=mid+1
        #if given 0 .that is only way we will get here
        return 0
                
