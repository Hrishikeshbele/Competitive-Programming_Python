'''
Longest Common Subsequence

Problem Description

Given two strings A and B. Find the longest common sequence ( A sequence which does not need to be contiguous), which is common in both the strings.

You need to return the length of such longest common subsequence.
Input 1:

 A = "abbcdgf"
 B = "bbadcgf"


Example Output
Output 1:

 5

Example Explanation
Explanation 1:

 The longest common subsequence is "bbcgf", which has a length of 5
 
 idea: to understand the solution approach watch the video by bak to back swe youtube channel. he explained solution approach this problem beatifully . 
 
 '''
 
 class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def solve(self, A, B):
        A=' '+A
        B=' '+B
        ans=[[0 for i in range(len(A))] for j in range(len(B))]
        for i in range(1,len(A)):
            for j in range(1,len(B)):
                if not B[j] or not A[i]:
                    ans[i][j]=0
                elif A[i]==B[j]:
                    ans[i][j]=ans[i-1][j-1]+1
                elif A[i]!=B[j]:
                    ans[i][j]=max(ans[i-1][j],ans[i][j-1]) # we will get max substring by taking max substring we get if we remove last char from either of string.
        return ans[-1][-1]
        
## solution 2 (recursive)

def lcs(a,b):
    if not a or not b:
        return 0
    if a[-1]==b[-1]: # if last element are equal to increment ans by 1 and decrease the srtring size. 
        return 1+lcs(a[:-1],b[:-1]) 
    else:
        return max(lcs(a[:-1],b),lcs(a,b[:-1])) # we will get max substring by taking max substring we get if we remove last char from either of string.
