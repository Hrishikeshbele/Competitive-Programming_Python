'''
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its minimum depth = 2.
solution: we find the height of left and right subtree by iteratively adding 1 every time.if either of subtree is not present return 1+ depth of existing subtree.
if both subtrees are present then return 1+min of subtree heights.1 here is for root node.
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
                return 0
        l=self.minDepth(root.left)
        r=self.minDepth(root.right)
        if not l or not r:
            return 1+l+r
        return 1+min(l,r)
            
