'''
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]

idea here is at each itereation we take values of current level nodes and  maintain list of next level nodes by keeping left and right node of each nodes in curr level nodes list.
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ret = [] # final answer list
        level = [root] #list to keep track of nodes in one layer

        while root and level:
            currentNodes = [] # list of node values of curr layer
            nextLevel = [] # keep track of nodes of next level
            for node in level: 
                # append to curr node val list
                currentNodes.append(node.val)
                # append next levl nodes
                if node.left:
                    nextLevel.append(node.left)
                if node.right:
                    nextLevel.append(node.right)
            # append this level nodes to final ans list
            ret.append(currentNodes)
            level = nextLevel


        return ret
                
        
