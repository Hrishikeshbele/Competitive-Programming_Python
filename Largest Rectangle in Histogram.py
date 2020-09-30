'''
Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.

Input: [2,1,5,6,2,3]
Output: 10

we solve it using the concept of smallest num to left and right  for each element and then substract left from right and multiply it by input elm height to get area.

'''
class Solution(object):
    def largestRectangleArea(self, a):
        """
        :type heights: List[int]
        :rtype: int
        """
        if not a:
            return 0
        if len(a)==1:
            return a[0]
        def lsr(a):
            stack=[]
            ans=[]
            for i in range(len(a)-1,-1,-1):
                if not stack:
                    ans.append(len(a))
                elif stack and stack[-1][0]<a[i]:
                    ans.append(stack[-1][1])
                elif stack and stack[-1][0]>a[i]:
                    while stack and stack[-1][0]>=a[i]:
                        stack.pop()
                    if stack:
                        ans.append(stack[-1][1])
                    elif not stack:
                        ans.append(len(a))
                stack.append((a[i],i))
            return ans[::-1]

        def nsl(a):
            ans=[]
            stack=[]
            for i in range(len(a)):
                if not stack:
                    ans.append(-1)
                elif stack[-1][0]<a[i]:
                    ans.append(stack[-1][1])
                elif stack[-1][0]>a[i]:
                    while stack and stack[-1][0]>=a[i]:
                        stack.pop()
                    if stack:
                        ans.append(stack[-1][1])
                    elif not stack:
                        ans.append(-1)
                stack.append((a[i],i))
            return ans

        
        ans=[] # width array
        for i,j in zip(lsr(a),nsl(a)):
            ans.append(i-j-1)
        #print(lsr(a),nsl(a))
        return (max(i*j for i,j in zip(ans,a)))
       
        
