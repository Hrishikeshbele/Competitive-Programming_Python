'''
Given a string S of lowercase letters, a duplicate removal consists of choosing two adjacent and equal letters, and removing them.
Input: "abbaca"
Output: "ca"
'''
'''
idea:
Loop on characters in the string S one by one.
If the next character is the same as the last in res, pop the last character from s.
Otherwise append the the next character to the end of s.
'''
class Solution(object):
    def removeDuplicates(self, S):
        """
        :type S: str
        :rtype: str
        """
        s=[]
        for i,val in enumerate(S):
            if s and s[-1]==val:
                s.pop()
            else:
                s.append(val)
        return ''.join(s)
        
