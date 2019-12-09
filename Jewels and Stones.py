'''
You're given strings J representing the types of stones that are jewels, and S representing the stones you have.  Each character in S is a 
type of stone you have.  You want to know how many of the stones you have are also jewels.
The letters in J are guaranteed distinct, and all characters in J and S are letters. Letters are case sensitive, so "a" is considered a 
different type of stone from "A".

Example 1:
Input: J = "aA", S = "aAAbbbb"
Output: 3
explaination: a is present 1 time and A is present 2 times in a S string
'''
solution1:
#brute force 
class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        count=0
        for i in J:
            for j in S:
                if i==j:
                    count+=1
        return count
        
        
solution2:
#here we are summing up count of each elm of J in S , x.count(y) find count of y in x
def numJewelsInStones(self, J, S):
    return sum(map(S.count, J))
