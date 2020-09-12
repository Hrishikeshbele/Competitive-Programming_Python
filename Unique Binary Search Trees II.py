'''
Given an integer n, generate all structurally unique BST's (binary search trees) that store values 1 ... n.

Example:

Input: 3
Output:
[
  [1,null,3,2],
  [3,2,null,1],
  [3,1,null,null,2],
  [2,1,3],
  [1,null,2,null,3]
]
Explanation:
The above output corresponds to the 5 unique BST's shown below:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
   
   
'''

def generateTrees(self, n):
    def node(val, left, right):
        node = TreeNode(val)
        node.left = left
        node.right = right
        return node
    def trees(first, last):
        return [node(root, left, right)
                for root in range(first, last+1)
                for left in trees(first, root-1)
                for right in trees(root+1, last)] or [None]
    return trees(1, n)
