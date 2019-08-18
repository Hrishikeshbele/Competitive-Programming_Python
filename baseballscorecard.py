'''
Given a list of strings, each string can be one of the 4 following types:

Integer (one round's score): Directly represents the number of points you get in this round.
"+" (one round's score): Represents that the points you get in this round are the sum of the last two valid round's points.
"D" (one round's score): Represents that the points you get in this round are the doubled data of the last valid round's points.
"C" (an operation, which isn't a round's score): Represents the last valid round's points you get were invalid and should be removed.
You need to return the sum of the points you could get in all the rounds.
Input: ["5","2","C","D","+"]
Output: 30
'''
class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        st=[]
        for i in ops:
            if i=='C':
                st.pop()
            elif i=='D':
                st.append(st[-1]*2)
            elif i=='+':
                st.append(st[-1]+st[-2])
            else:
                st.append(int(i))
        return sum(st)
