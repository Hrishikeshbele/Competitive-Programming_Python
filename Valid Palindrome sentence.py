'''
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
solution appoach:we use 2 pointer technique every time we check if letter is alphanumeric if not we increment counter and check where char 
are alphanumeric.
'''

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        start,end=0,len(s)-1
        while start<end:
            #if letter is not alphanumeric then just increase or decrease the pointer
            if not s[start].isalnum():
                start+=1
            elif not s[end].isalnum():
                end-=1
            #if letters from end and start both are alphanumeric we check if both are equal 
            #if equal we increment and decrement counter respectively
            else:
                if s[start].lower()!=s[end].lower():
                    return False
                else:
                    start+=1
                    end-=1
        return True
