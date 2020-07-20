'''
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]

idea: first we sorted the element of strs list then we checked if sorted str already exist as dict key if yes we will append current element to its value list else we will create list 
with current str element. we sort the string because all anograms will be same string once sorted.
'''
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dicts={}
        for t in (strs):
            key=''.join(sorted(t))
            if key in dicts:
                dicts[key].extend([t])
            else:
                dicts[key]=[t]
        return list(dicts.values())
