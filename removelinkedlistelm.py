'''
Remove all elements from a linked list of integers that have value val.

Example:

Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5
'''
'''
approach:
In order to save the need to treat the "head" as special, the algorithm uses a "dummy" head. This simplifies the code greatly, 
particularly in the case of needing to remove the head AND some of the nodes immediately after it.
Then, we keep track of the current node we're up to, and look ahead to its next node, as long as it exists. If current_node.next does need removing, then we simply replace it with current_node.next.
next. We know this is always "safe", because current_node.next is definitely not None (the loop condition ensures that), so we can safely access its next.
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        dummy=ListNode(-1)
        #assigning next of dummy node to head
        dummy.next=head
        curr=dummy
        while curr.next:
            #if next node val is to be deleted then assign curr node next to next.next 
            if curr.next.val==val:
                curr.next=curr.next.next
            else:
                #if curr node value not to be deleted advance to next node
                curr=curr.next
           
        return dummy.next
            
        

        
