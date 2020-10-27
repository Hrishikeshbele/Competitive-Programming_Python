'''
Problem Description

Given two Binary Trees A and B, you need to merge them in a single binary tree.

The merge rule is that if two nodes overlap, then sum of node values is the new value of the merged node.

Otherwise, the non-null node will be used as the node of new tree.


Example 1:

Input: 
	Tree 1                     Tree 2                  
          1                         2                             
         / \                       / \                            
        3   2                     1   3                        
       /                           \   \                      
      5                             4   7                  
Output: 
Merged tree:
	     3
	    / \
	   4   5
	  / \   \ 
	 5   4   7
   
   
   
  idea here is we will add values from each trees if values is present in both trees otherwise we will just use whichever value is present
  
  '''
  
  class Solution:
    # @param A : root node of tree
    # @param B : root node of tree
    # @return the root node in the tree
    def solve(self, A, B):
        new=TreeNode(None)
        if A and B:
            new.val=A.val+B.val
            new.left=self.solve(A.left,B.left)
            new.right=self.solve(A.right,B.right)
            return new
        else:
            return A or B

# same as above approach 
class Solution(object):
    def mergeTrees(self, A, B):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        ans=TreeNode(None)
        if not A and not B:
            return None
        if not A or not B:
            return A or B
        if A and B:
            ans.val= A.val+B.val      
            ans.left=self.mergeTrees(A.left,B.left)
            ans.right=self.mergeTrees(A.right,B.right)
        
        return ans
