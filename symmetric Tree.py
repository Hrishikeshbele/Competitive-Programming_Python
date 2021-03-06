'''
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3

2 trees T1 and T2 are symmetric if
1) value of T1’s root is same as T2’s root
2) T1’s left and T2’s right are symmetric.
3) T2’s left and T1’s right are symmetric.

'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        #funtion to check if left and right child of root node are reflection of each other
        def is_mirror(L,R):
            if not L and not R:
                return True
            if L and R and L.val == R.val: 
                return is_mirror(L.left, R.right) and is_mirror(L.right, R.left)
            return False

        
        return is_mirror(root,root)
        
        
