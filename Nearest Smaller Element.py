'''
Given an array, find the nearest smaller element G[i] for every element A[i] in the array such that the element has an index smaller than i.
Input : A : [4, 5, 2, 10, 8]
Return : [-1, 4, -1, 2, 2]
'''
class Solution:
	# @param A : list of integers
	# @return a list of integers
	def prevSmaller(self, A):
        #maintaining stack of smaller elm's than curr elm from left side of curr elm
	    stack=[]
      #creating new stack to store result
	    result=[]
	    for i in range(len(A)):
          #removing all elm greater than curr elm from left of curr elm
	        while stack and stack[-1]>=A[i]:
	            stack.pop()
          #if stack is not empty we append it's last elm to result
	        if stack:
	            result.append(stack[-1])
          #if no elm smaller than A[i] to left side then append -1 to result
	        else:
	            result.append(-1)
	        stack.append(A[i])
	    return result
