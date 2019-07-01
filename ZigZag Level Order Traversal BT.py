'''
Given a binary tree, return the zigzag level order traversal of its nodes’ values. (ie, from left to right, then right to left for the next level and alternate between).

Example : 
Given binary tree

    3
   / \
  9  20
    /  \
   15   7
return

[
         [3],
         [20, 9],
         [15, 7]
]
'''
# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of list of integers
    def zigzagLevelOrder(self, A):
        values = []
        queue = [ ( A, 0 ) ]
        while queue:
            node, depth = queue.pop(0)
            if node:
                if len(values) < depth + 1:
                    values.append([])
                if depth % 2:
                    values[depth].insert(0, node.val)
                else:
                    values[depth].append(node.val)
                queue.append(( node.left, depth + 1 ))
                queue.append(( node.right, depth + 1 ))
        return values

