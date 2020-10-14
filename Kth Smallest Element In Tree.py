'''
Given a binary search tree, write a function to find the kth smallest element in the tree.
'''
# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return an integer
    def kthsmallest(self,root, k):
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            #decrease 1 for every greater smallest elm
            k -= 1
            #if k==0 means we arrived at our kth smallest number
            if k == 0:
                return root.val
            root = root.right
        
            
# solution2

    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        def helper(root,ans):
            if root:
                helper(root.left,ans)
                ans.append(root.val)
                helper(root.right,ans)
            return ans
        
        return helper(root,[])[k-1]
