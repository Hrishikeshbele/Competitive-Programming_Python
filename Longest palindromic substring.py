'''
Given a string S, find the longest palindromic substring in S.

Input : "aaaabaaa"
Output : "aaabaaa"
'''
#If substring s[i+1..j-1] is a palindrome, then string s[i..j] is palindrome if and only if s[i] = s[j].
def longestPalindrome(s):
    M=[[False]*len(s) for i in range(len(s))]
    # if length of string is 1.since all substring of len 1 will be palindromic
    maxl=1
    start=0
    for i in range(len(s)):
        M[i][i]=True
    #for len==2.string of len 2 will be pelindromic if first and second char are equal
    for i in range(len(s)-1):
        if s[i]==s[i+1]:
            M[i][i+1]=True
            start=i
            maxl=2
    #for len>2
    #To calculate table[i][j],if the value of table[i+1][j-1] and str[i] is same as str[j] then we make table[i][j] true
    #k is len of substring
    for k in range(3,len(s)+1):
        #i is starting index of string,i can be for 0th char to 
        # (len(s)-k+1) char to make string of len k.
        for i in range(len(s)-k+1):
            #index of last char of string 
            j=i+k-1
            print(s[i:j+1])
            if (M[i+1][j-1] and s[i]==s[j]):
                M[i][j]=True
                if k>maxl:
                    start=i
                    maxl=k
    return s[start:start+maxl]

#solution2
'''
idea:
at each elm we go left and right and see how much longest substring is possible.if that string has length more that max len string until now. we update the max str.
(why a[l+1:r]?)  :The while loop stops either because l or r is out of range or because the s[l] != s[r], which means neither s[l] nor s[r] can be part of the longest palindrome and 
the helper function returns s[l+1:r](inclusive on the left and exclusive on the right).
'''

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        res=''
        for i in range(len(s)):
            # (s,i,i) for odd case, like "aba"  
            # (s,i,i+1) for even case, like "abba"
            res=max(self.helper(s,i,i),self.helper(s,i,i+1),res,key=len)
        return res
    # get the longest palindrome, l, r are the middle indexes from inner to outer
    def helper(self,s,l,r):
        while l>=0 and r<len(s) and s[l]==s[r]:
            l-=1
            r+=1
        return s[l+1:r] #return 1 step back from front and back since curr pair doesn't
                            # satisfy palindrome prop
        
        
