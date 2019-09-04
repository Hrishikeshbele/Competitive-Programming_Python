'''
Given a non-empty string check if it can be constructed by taking a substring of it and appending multiple copies of the substring together. You may assume the given string consists of lowercase English letters only and its length will not exceed 10000.

 

Example 1:

Input: "abab"
Output: True
Explanation: It's the substring "ab" twice.
'''
'''
idea:
Consider a string S="helloworld". Now, given another string T="lloworldhe", can we figure out if T is a rotated version of S? 
Yes, we can! We check if S is a substring of T+T.

The maximum length of a "repeated" substring that you could get from a string would be half it's length
For example, s = "abcdabcd", "abcd" of len = 4, is the repeated substring.
You cannot have a substring >(len(s)/2), that can be repeated.
So, when ss = s + s , we will have atleast 4 parts of "repeated substring" in ss.
(s+s)[1:-1], With this we are removing 1st char and last char => Out of 4 parts of repeated substring, 2 part will be gone (they will no longer have the same substring).
ss.find(s) != -1, But still we have 2 parts out of which we can make s. And that's how ss should have s, if s has repeated substring.
'''

def repeatedSubstringPattern(self, str):

        """
        :type str: str
        :rtype: bool
        """
        if not str:
            return False
            
        ss = (str + str)[1:-1]
        return ss.find(str) != -1
