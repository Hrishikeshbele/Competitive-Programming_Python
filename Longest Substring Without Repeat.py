'''
Given a string, 
find the length of the longest substring without repeating characters.

Example:

The longest substring without repeating letters for "abcabcbb" is "abc", which the length is 3.

idea: watch video by datadaft on youtube.
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
        
#solution-2
# idea is to store the each chart and its prev seen position as dict and if we encounter a repeated char we start with new string and for each string and each increasing char we keep track of max length of string we encounterd
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        dicts={}
        #start var to keep track of start of new substring after repeating charecters
        start=max_len=0
        for i,val in enumerate(s):
            if val in dicts and dicts[val]>=start :
                # we move one char forward from last seen postion of char
                start=dicts[val]+1
          
            else:
                max_len=max(max_len,i-start+1)	
            #storing last seen pos of char in dict 
            dicts[val]=i
        return max_len
  
        
