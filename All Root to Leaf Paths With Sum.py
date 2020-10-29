'''
Given a binary tree and a sum, find all root-to-leaf paths where each path’s sum equals the given sum.

For example:
Given the below binary tree and sum = 22,

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
return

[
   [5,4,11,2],
   [5,8,4,5]
]

'''

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return a list of list of integers
    def pathSum(self, A, B):
        res = [] #global var
        def solve(curr_set,curr_sum,node):
            if node is None:
                return 
            if node.right is None and node.left is None:
                if curr_sum+node.val==B:
                    res.append(curr_set+[node.val])
                    return
                
            solve(curr_set+[node.val],curr_sum+node.val,node.left)
            solve(curr_set+[node.val],curr_sum+node.val,node.right)
        solve([],0,A)
        return res
