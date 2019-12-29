'''
Given a string s and a string t, check if s is subsequence of t.
A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters 
without disturbing the relative positions of the remaining characters. (ie, "ace" is a subsequence of "abcde" while "aec" is not).

solution approach: we find the index of elms of s in t if present and then we decrease the list t upto  indx of curr elm of s to check 
presence of elm of s in oredered manner in t
''' 


class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        for i in s:
            #finding index of elm of s in t if present 
            ind=t.find(i)
            #if elm is not present return false
            if ind==-1:
                return False
            else:
                #we remove the elms in list t upto  indx of curr elm i. so that we can 
                #insure elm in s are present in order in t
                t=t[ind+1:]
        return True
        
        
