'''
Given a string, 
find the length of the longest substring without repeating characters.

Example:

The longest substring without repeating letters for "abcabcbb" is "abc", which the length is 3.
'''
class Solution:
    # @param A : string
    # @return an integer
    def lengthOfLongestSubstring(self,s):
        dic, res, start, = {}, 0, 0
        for i, ch in enumerate(s):
            if ch in dic:
                # update the res, len of longest string (curr ind - start of curr str)
                res = max(res, i-start)
            
            # updating the start of curr sting every-time 
            # here should be careful, like "abba"
                start = max(start, dic[ch]+1)
            dic[ch] = i
        
    # return should consider the last 
    # non-repeated substring
        return max(res, len(s)-start)
        
