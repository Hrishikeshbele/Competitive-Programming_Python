'''
Given the head of a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.
Input: head = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: One possible answer is [0,-3,9,-10,null,5], which represents the shown height balanced BST.

i first got the node values from linked list into one list and then i created tree using binary search approach where mid elm is assigned as root node and left and right node is passed
with recursive binary search call over left and right halfs.

'''

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        #getting linked list node values
        if not head:
            return None
        res=[]
        while head and head.next:
            res.append(head.val)
            head=head.next
        res.append(head.val)
        # helper function for binary search tree formation
        def helper(start,end,res):
            if start > end:
                return None
            mid=(start+end)//2
            node=TreeNode(res[mid])
            node.left=helper(start,mid-1,res)
            node.right=helper(mid+1,end,res)
            return node
        return helper(0,len(res)-1,res)
            
            
            
# solution 2( using fast and slow pointers)

# recursively
def sortedListToBST(self, head):
    if not head:
        return 
    if not head.next:
        return TreeNode(head.val)
    # here we get the middle point,
    # even case, like '1234', slow points to '2',
    # '3' is root, '12' belongs to left, '4' is right
    # odd case, like '12345', slow points to '2', '12'
    # belongs to left, '3' is root, '45' belongs to right
    slow, fast = head, head.next.next
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    # tmp points to root
    tmp = slow.next
    # cut down the left child
    slow.next = None
    root = TreeNode(tmp.val)
    root.left = self.sortedListToBST(head)
    root.right = self.sortedListToBST(tmp.next)
    return root
        
