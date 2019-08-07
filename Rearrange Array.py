'''
Rearrange a given array so that Arr[i] becomes Arr[Arr[i]] with O(1) extra space.

Example:

Input : [1, 0]
Return : [0, 1]

'''
class Solution:
    # @param A : list of integers 
    def arrange(self, A):
        ans=[]
        S=A
        for i in S :
            ans.append(A[i])
        return ans 


