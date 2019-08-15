'''
Given 2 sorted arrays, find all the elements which occur in both the arrays.
Example :
Input : 
    A : [1 2 3 3 4 5 6]
    B : [3 3 5]

Output : [3 3 5]
'''
class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @return: a list of integers
    def intersect(self, A, B):
        ans=[]
        i,j=0,0
        #if elm in 2 arr are same we are appending it and increamenting i,j by 1,when a[i]>b[j] we increament j since arr are sorted 
        while(i<len(A) and j<len(B)):
            if B[j]==A[i]:
                ans.append(A[i])
                i+=1
                j+=1
            elif A[i]>B[j]:
                j+=1
                
            elif B[j]>A[i]:
                i+=1
        return ans
