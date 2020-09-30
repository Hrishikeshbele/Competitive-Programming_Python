'''
Problem Description

Given a string A, find the common palindromic sequence ( A sequence which does not need to be contiguous and is a pallindrome), which is common in itself.

You need to return the length of longest palindromic subsequence in A.
Input 1:

 A = "bebeeed"


Example Output
Output 1:

 4


Example Explanation
Explanation 1:

 The longest common pallindromic subsequence is "eeee", which has a length of 4
 
 
 we use the technique of longest common susequence problem. 
 '''
 
 class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        def lcs(a,b):
            a=' '+a
            b=' '+b
            ans=[[0 for i in range(len(a))] for j in range(len(b))]
            for i in range(1,len(a)):
                for j in range(1,len(b)):
                    if not a[i] or not b[j]:
                        ans[i][j]= 0
                    elif a[i]==b[j]:
                        ans[i][j]=ans[i-1][j-1]+1
                    else:
                        ans[i][j]=max(ans[i-1][j],ans[i][j-1])
            return ans[-1][-1]
        return lcs(A,A[::-1]) # pass string and its reverse string to lcs function
