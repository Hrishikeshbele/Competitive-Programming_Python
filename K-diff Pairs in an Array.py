'''
Given an array of integers and an integer k, you need to find the number of unique k-diff pairs in the array. Here a k-diff pair is defined as an integer pair (i, j), where i and j are both numbers in the array and their absolute difference is k.

Example 1:
Input: [3, 1, 4, 1, 5], k = 2
Output: 2
Explanation: There are two 2-diff pairs in the array, (1, 3) and (3, 5).
Although we have two 1s in the input, we should only return the number of unique pairs.

'''
from collections import Counter
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
		#If k is less than 0, then the result is 0 since we are looking fpr pairs with an ABSOLUTE difference of k.
        if k < 0:
            return 0
        
        count = Counter(nums)
        pairs = set([])
        
        for num in count.keys():
			#Special case: If k == 0, then there needs to be at least two occurences of a particular num in nums 
			#in order for there to be a pair (num, num).
            if k == 0:
                if count[num] > 1:
                    pairs.add((num, num))
					
			#Regular case: k != 0. Simply check if num + k is a member of the array nums.
			#Insert the pair into the set of pairs (smallerNum, largerNum) so that there are no duplicate pairs.
            else:
                otherNum = num + k
                if otherNum in count:
                    pairs.add((num, otherNum) if num <= otherNum else (otherNum, num))
                    
        return len(pairs)

# solution 2 (with 2 pointers techs)

def findPairs(self, a, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        a.sort()
        ans=set()
        i,j=0,1
	 """
        Special Case: k = 0 # below code will include same elm 2 time as pair(when i==j) which we don't want
        - Use the Python collections Counter to get the frequency
          of each value in nums.
        - Determine the number of zero differences by counting
          the number of values in nums with frequency > 1.
        """
        if k == 0:
            freqs = Counter(a)
            return sum(freqs[k] > 1 for k in freqs)
	 """
        General Case: k > 0
        - produce a sorted list of values
        - Use two pointers (slow and fast) in a sliding window
          protocol to find all pairs whose difference is k.
          - If difference is smaller than k, advance fast pointer.
          - If difference is larger than k, advance slow pointer.
          - If difference equals k, advance both pointers and
            increment a counter that is later returned from this
            program.
        """
        while  j<len(a):
            if abs(a[j]-a[i])==k:
                ans.add((a[i],a[j]))
                i+=1
                j+=1
            elif a[j]-a[i]<k:
                j+=1
            else:
                i+=1
        return len(ans)
