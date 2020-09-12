'''
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]

idea here is at each itereation we take values of current level nodes and  maintain list of next level nodes by keeping left and right node of each nodes in curr level nodes list.
before appending curr layer nodes to final list we check if need to transverse from right or left on one var value. if right transversal then we just reverse the curr nodes list.
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ans=[] # list to store final ans
        layer=[root] # list to store curr ans
        rev=False # var to keep track of if we need to reverse the list at this level
        while root and layer:
            curr=[] # list of node values of curr layer
            nexl=[] # keep track of nodes of next level
            for node in layer:
                curr.append(node.val)
                if node.left:
                    nexl.append(node.left)
                if node.right:
                    nexl.append(node.right)
            # append this level nodes to final ans list based on rev var value
            if rev:
                ans.append(curr[::-1])
                rev=False
            else:
                ans.append(curr)
                rev=True
            layer=nexl
        return ans
