'''
Given a string S, find the longest palindromic substring in S.

Substring of string S:

S[i...j] where 0 <= i <= j < len(S)

Palindrome string:

A string which reads the same backwards. More formally, S is palindrome if reverse(S) = S.

Incase of conflict, return the substring which occurs first ( with the least starting index ).

Example :

Input : "aaaabaaa"
Output : "aaabaaa"

idea:
at each elm we go left and right and see how much longest substring is possible.if that string has length more that max len string until now. we update the max str.
(why a[l+1:r]?)  :The while loop stops either because l or r is out of range or because the s[l] != s[r], which means neither s[l] nor s[r] can be part of the longest palindrome and 
the helper function returns s[l+1:r](inclusive on the left and exclusive on the right).
'''

class Solution:
    # @param A : string
    # @return a strings
    def longestPalindrome(self, a):
        def helper(l,r):
            while l>=0 and r<len(a) and a[l]==a[r]:
                l-=1
                r+=1
                
            return a[l+1:r] #return 1 step back from front and back since curr pair doesn't
                            # satisfy palindrome prop
                
        ans=''
        for i in range(len(a)):
            # longest string with odd no of chars
            temp=helper(i,i)
            if len(temp)>len(ans):
                ans=temp
            #if longest string cont even no of chars
            temp=helper(i,i+1)
            if len(temp)>len(ans):
                ans=temp
       
        return ans
        
            
            
