'''
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example:

Given the sorted array: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5
 
solution idea: using idea that mid elm is root,we recursively form left and right subtrees by passing left and right lists around mid elm resp
 '''
 
 # Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        
        def convert(nums,left,right):
            if left>right:
                return None
            mid=(left+right)//2
            root=TreeNode(nums[mid])
            root.left=convert(nums,left,mid-1)
            root.right=convert(nums,mid+1,right)
            return root
        return convert(nums,0,len(nums)-1)
