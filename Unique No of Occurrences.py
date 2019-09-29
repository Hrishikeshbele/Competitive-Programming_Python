'''
Given an array of integers arr, write a function that returns true if and only if the number of occurrences of each value in the array is unique.


Example 1:

Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.
Example 2:

Input: arr = [1,2]
Output: false
'''

class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        # we are first counting the no of occurences of each elm and storing it in list. then if len of set of this list is equal to 
        # length of set of actual array we can say that occurance of every elm is unique.
        count=[arr.count(x) for x in arr]
        return (len(set(arr))==(len(set(count))))
        
