'''
Palindrome String
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Example:

"A man, a plan, a canal: Panama" is a palindrome.

"race a car" is not a palindrome.

Return 0 / 1 ( 0 for false, 1 for true ) for this problem

idea here is simple first we split the string using space operator then we remove the not alphnumeric char from each substring and join them and then check for palindrome.

'''
class Solution:
    # @param A : string
    # @return an integer
    def isPalindrome(self, A):
        A=A.lower()
        lst=A.split(' ')
        ans=[]
        for k in lst:
            # if all char in curr num are not alphnumeric
            if not k.isalnum():
                #take only alphanumeric char of string
                ans.append(''.join([i for i in k if i.isalnum()]))
            else:
                ans.append(k)
        # check for palindrome property
        if ''.join(ans)==''.join(ans)[::-1]:
            return 1
        else:
            return 0
