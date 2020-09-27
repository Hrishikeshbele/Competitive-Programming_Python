'''
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        return 1+max(self.maxDepth(root.left),self.maxDepth(root.right)) # we are adding 1 each time we are trasversing downward

    
# above solution can be written in following way
class Solution:
    # @param A : root node of tree
    # @return an integer
    def maxDepth(self, A):
        if A:
            return 1+max(self.maxDepth( A.left),self.maxDepth( A.right))
        else:
            return 0
