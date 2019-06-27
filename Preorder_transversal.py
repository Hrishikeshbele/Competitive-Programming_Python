'''
Given a binary tree, return the preorder traversal of its nodes’ values.

Example :
Given binary tree

   1
    \
     2
    /
   3
return [1,2,3].
'''
#solution using recursion
# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

class Solution:
	# @param A : root node of tree
	# @return a list of integers
	def preorderTraversal(self, start):
	    res=[]
        if start:
            res.append(start.val)
            res += (self.preorderTraversal(start.left))
            res += (self.preorderTraversal(start.right))
        return res
#without recursion using stacks
class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def preorderTraversal(self, start):
        stack=[start]
        res=[]
        while stack:
            root=stack.pop()
            res.append(root.val)
            if root.right:
                stack.append(root.right)
            if root.left:
                stack.append(root.left)
            
        return res
