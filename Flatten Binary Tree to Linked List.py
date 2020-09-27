'''
Given a binary tree, flatten it to a linked list in-place.

For example, given the following tree:

    1
   / \
  2   5
 / \   \
3   4   6
The flattened tree should look like:

1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6
          
 answer explaination: 
          
we will use the concept of reverse preorder traversal. we will travel to rightmost node of tree first then we will remember that node as prev node and next time we will go to its left node
and assign root as curr left node and right node as prev node. 
DFS traversal with the ordering: ( Right node, Left node, Current node )

1.Change current node's right child as previous traversal node.
2.Change current node's left child as None(i.e., NULL)
3. Update previous traversal node as current node
ex.
root
    / 
  1 
 / \ 
3  4  
Let's see what is happening with this code.

Node(4).right = None
Node(4).left = None
prev = Node(4)
Node(3).right = Node(4) (prev)
Node(3).left = None
prev = Node(3)->Node(4)
Node(1).right = prev = Node(3) -> Node(4)
Node(1).left = None
prev = Node(1)->Node(3)->Node(4) (Which is the answer)
The answer use self.prev to recode the ordered tree of the right part of current node.
Remove the left part of current node

'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        self.previous_right = None

        def helper(root):
            if root:
                helper(root.right)
                helper(root.left)
                root.right, self.previous_right = self.previous_right, root
                root.left=None
               
        helper(root)
        
# solution using preorder transversal

class Solution:
    # @param A : root node of tree
    # @return the root node in the tree
    def preorder(self,A,ans):
        if(not A):
            return
        
        ans.append(A.val)
        self.preorder(A.left,ans)
        self.preorder(A.right,ans)
        
        return(ans)
        
    def flatten(self, A):
        arr=self.preorder(A,[])
        d=TreeNode(None)
        new=d
        for i in arr:
            node=TreeNode(i)
            new.right=node
            new=new.right
        return(d.right)
