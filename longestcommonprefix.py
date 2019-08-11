'''
Given the array of strings A, 
you need to find the longest string S which is the prefix of ALL the strings in the array.

Longest common prefix for a pair of strings S1 and S2 is the longest string S which is the prefix of both S1 
and S2.

For Example, longest common prefix of "abcdefgh" and "abcefgh" is "abc".

'''
class Solution:
    # @param A : list of strings
    # @return a strings
    def longestCommonPrefix(self, A):
        if not A:
            return ''
        if len(A)==1:
            return A[0]
        ans=''
        for i in range(min(map(len,A))):
        #all returns true if all elms are true in iterable
            if all(s[i]==min(A,key=len)[i] for s in A):
                ans=ans+str(A[0][i])
            else:
                break
        return ans
