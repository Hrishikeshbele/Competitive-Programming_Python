'''
Problem Description

Given an one-dimensional unsorted array A containing N integers.

You are also given an integer B, find if there exists a pair of elements in the array whose difference is B.

Return 1 if any such pair exists else return 0.
Example Input
Input 1:

 A = [5, 10, 3, 2, 50, 80]
 B = 78
Explanation 1:

 Pair (80, 2) gives a difference of 78.
 
 idea  here is use 2 pointers. one pointing to 1st elm and other two second elm. first sort the array and then look for 2 elm whose diff is target using 2 pointers.
 
 '''
 class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        A=sorted(A)
        i,j=0,1
        while i<len(A) and j<len(A):
            if j!=i and A[j]-A[i]==B:
                return 1
            elif A[j]-A[j]<B:
                j+=1
            else:
                i+=1
        return 0
