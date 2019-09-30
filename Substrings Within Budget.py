'''
You are given two strings s and t of the same length. You want to change s to t. Changing the i-th character of s to i-th character of t costs |s[i] - t[i]| that is, the absolute difference between the ASCII values of the characters.

You are also given an integer maxCost.

Return the maximum length of a substring of s that can be changed to be the same as the corresponding substring of twith a cost less than or equal to maxCost.

If there is no substring from s that can be changed to its corresponding substring from t, return 0.

Example 1:

Input: s = "abcd", t = "bcdf", maxCost = 3
Output: 3
Explanation: "abc" of s can change to "bcd". That costs 3, so the maximum length is 3.

'''

class Solution(object):
    def equalSubstring(self, s, t, maxCost):
        """
        :type s: str
        :type t: str
        :type maxCost: int
        :rtype: int
        """
        diff=[]
        sum_=0
        lo,width=-1,0
        #calculating the diff between ordinal values of corrspnd char of 2 str's
        for k,l in zip(s,t):
                diff.append(abs(ord(k)-ord(l)))
        #using sliding window technique:
        for hi in range(len(diff)):
            #keep decreasing the cost on lo end and ...
            maxCost=maxCost-diff[hi]
            # if the cost is higher than maxCost, then shrink widow by removing element from lo end;we increase the value of lo here.
            if  maxCost <0:
                lo+=1
                maxCost+=diff[lo]
            #Update the max window width during each iteration.
            width=max(width, hi-lo)
        return width
